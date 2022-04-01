from flask import render_template, request, Blueprint
from chatbot.main.ai import chatb


main = Blueprint('main', __name__)


@main.route("/")
def home():
    return render_template("index1.html")


@main.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatb.get_response(userText))