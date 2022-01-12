
import speech_recognition as sr
from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    # Route for the index page
    return render_template('index.html') 
    
@app.route ("/erro")
def erro():
    # Error page for misinterpretention of what was said
    return render_template('erro.html')

@app.route ("/exception")
def exception():
    # Exception page if the recognizer throws an exception (for example if nothing is said)
    return render_template('exception.html')

@app.route("/page", methods = ['GET', 'POST'])
def page():
    # Post request comes from the button of the index page
    if request.method == 'POST':
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        key = False
        
        try:
            # Reocgnizer will listen using the computer's microphone
            with mic as source:
                audio = recognizer.listen(source)
            # Speech will be transcripted by google's API
            command = recognizer.recognize_google(audio, language = 'pt-BR')
            print (command)
            # Saying "oi" (hi) will load a new page
            if command == "Oi":
                return render_template ("page.html")
            # Saying "sim" (yes) will load the same page as above but with an extra message
            elif command == "sim":
                key = True
                return render_template ("page.html", key = key)
            # Saying anything else will load an error page
            else:
                return redirect('/erro')
        # Except will handle another issues from the recognizer and load a specific page
        except:
            return redirect('/exception')

