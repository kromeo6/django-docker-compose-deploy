# class chatb():
# 	def get_response(x):
# 		return 'test pasuxi'

import nltk
import os
#nltk.path.append('./nltk_data/')
print(os.getcwd())
#nltk.download('punkt', download_dir='./app/nltk_data/')
nltk.download('punkt', download_dir='/py/nltk_data/')
#nltk.download('punkt', download_dir='/usr/lib/nltk_data/')
#nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow
import numpy as np

from tensorflow.keras.models import load_model

model = load_model('core//main//ai_files//chatbot_model.h5')
import json
import random
intents = json.loads(open('core//main//ai_files//intents.json',encoding="utf8").read())
tf = json.loads(open('core//main//ai_files//matching.json',encoding="utf8").read())
words = pickle.load(open('core//main//ai_files//words.pkl','rb'))
classes = pickle.load(open('core//main//ai_files//classes.pkl','rb'))

tlist=tf["basewords"]

class prediction():
	def fudze(self, w):
	    for i in range(len(tlist)):
	        if w in tlist[i]['variation']:
	            res=tlist[i]['base']
	            break
	        else:
	            res=w
	    return res

	def clean_up_sentence(self, sentence):
	    sentence_words = nltk.word_tokenize(sentence)
	    sentence_words = [self.fudze(word.lower()) for word in sentence_words]
	    return sentence_words

	# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

	def bow(self, sentence, words, show_details=True):
	    # tokenize the pattern
	    sentence_words = self.clean_up_sentence(sentence)
	    # bag of words - matrix of N words, vocabulary matrix
	    bag = [0]*len(words)
	    for s in sentence_words:
	        for i,w in enumerate(words):
	            if w == s:
	                # assign 1 if current word is in the vocabulary position
	                bag[i] = 1
	                if show_details:
	                    print ("found in bag: %s" % w)
	    return(np.array(bag))

	def predict_class(self, sentence, model):
	    # filter out predictions below a threshold
	    p = self.bow(sentence, words,show_details=False)
	    res = model.predict(np.array([p]))[0]
	    ERROR_THRESHOLD = 0.5
	    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
	    # sort by strength of probability
	    results.sort(key=lambda x: x[1], reverse=True)
	    return_list = []
	    for r in results:
	        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
	    if len(return_list)==0:
	        return_list.append({'intent': 'noanswer', 'probability': '0.9'})        
	    return return_list

	def getResponse(self, ints, intents_json):
	    tag = ints[0]['intent']
	    list_of_intents = intents_json['intents']
	    for i in list_of_intents:
	        if(i['tag']== tag):
	            result = random.choice(i['responses'])
	            break
	    return result

	def chatbot_response(self, msg):
	    ints = self.predict_class(msg, model)
	    res = self.getResponse(ints, intents)
	    return res

  