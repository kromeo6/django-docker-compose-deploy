import logging
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.http import JsonResponse
from core.main.ai import prediction
from core.models import Chat
from datetime import datetime


#logger = logging.getLogger('main')
pred = prediction()

@csrf_exempt
def view1(request):
    #logger.info('hello')
    return HttpResponse('Hi There')

@csrf_exempt
def home(request):
    #logger.info('home page')
    return render(request, 'chatb/index.html')

@csrf_exempt
def get_bot_response(request, *args, **kwargs):

    if not request.session.session_key:
        request.session.create()
    print('esaaaa', request.session.session_key)
    userText = request.GET['msg']
    ses_key = request.session.session_key
    dt = str(datetime.utcnow())

   
    try:
        chat = Chat(session_id=ses_key, dt=dt, message=userText)
        chat.save()
    except:
        print('not saved in databases')
        #logger.info('not saved into db')
    


    #print(Chat.objects.all())
    #post = Post(message=str(userText))
    #print(post)
    #db.session.add(post)
    #db.session.commit()

    a = 'კოვიდის ხშირი სიმპტომებია: ცხელება, ხველა, დაღლილობის შეგრძნება, ასეთ შემთხვევაში უნდა დაუკავშირდეთ ექიმს და გაიკეთოთ ტესტი. ვირუსის თავიდან ასაცილებლად უნდა დაიცვათ ჰიგიენა და მოერიდოთ ხალხმრავალ ადგილებს.ვირუსის გადაცემა ხდება წვეთოვანი და კონტაქტური გზით-მაგალითად, ხველის ან ცემინების დროს, ხელის ჩამორთმევით.'
    b = 'ვაქცინაცია უფასოა და სავალდებულო არ არის, რეგისტრაციის გავლა შესაძლებელია აქ: <a href="http://www.booking.moh.gov.ge" target="_blank"> booking.moh.gov.ge </a>, დეტალური ინფორმაციისთვის ეწვიეთ: <a href="https://www.provax.ge" target="_blank"> provax.ge </a> . ვაქცინაციის შედეგად თქვენ იცავთ თავს და გარშემომყოფებს დაავადებისგან. ვაქცინების ნაწილი, მაგალითად PFIZER-ის და MODERNA-ს ვაქცინები მზადდება საინფორმაციო რნმ-ის გამოყენებით, მათ არ შეუძლიათ შეცვალონ ადამიანის დნმ. ვაქცინაცია უსაფრთხოა.'
    c = 'მოხალისედ რეგისტრაციისთვის რიგში საჭიროა მიჰყვეთ ინსტრუქციას ბმულზე: <a href="http://www.help.redcross.ge" target="_blank"> help.redcross.ge </a> . ჩვენ ადამიანებს ეტაპობრივად ვრთავთ, სხვადასხვა სახის აქტივობებში'
    d = 'მიმდინარე ეტაპზე ჩვენ ვეხმარებით მარტოხელა, სოციალურად დაუცველ 60-დან 70 წლამდე ასაკის პირებს; კოვიდ ვირუსის გამო თვითიზოლაციაში მყოფ პირებს. კრიტერიუმები პერიოდულად იცვლება, უფრო დაზუსტებული ინფორმაციისთვის დაგვიკავშირდით ცხელ ხაზზე.'
    e = 'წითელი ჯვრის საზოგადოებას საქართველოში ორმოცი ფილიალი აქვს. ცხელი ხაზის ნომრებია: ქალაქის ნომრებიდან უფასო: 032 2 501 105. ნებისმიერი ტელეფონიდან უფასო: 0 800 000 018.'

    if userText == 'one11':
        return JsonResponse({'ans': a})
    elif userText == 'two22':
        return JsonResponse({'ans': b})
    elif userText == 'two33':
        return JsonResponse({'ans': c})
    elif userText == 'two44':
        return JsonResponse({'ans': d})
    elif userText == 'two55':
        return JsonResponse({'ans': e})
    else:
        resp = str(pred.chatbot_response(msg=userText))
        return JsonResponse({'ans': resp})


