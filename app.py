
import speech_recognition as sr
import time
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
            with mic as source:
                audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language = 'pt-BR')
            print (command)
            if command == "Oi":
                return render_template ("page.html")
            elif command == "sim":
                key = True
                return render_template ("page.html", key = key)
            else:
                return redirect('/erro')
        except:
            return redirect('/exception')

    





#r = sr.Recognizer()

#test = sr.AudioFile('NeueAufnahme107.wav')

#with test as source:
#    audio = r.record(source)

#text = r.recognize_google(audio, language = 'pt-BR')

#print(text)

#output = open('test.txt', 'w')
#output.write(text)
#output.close()

#mic = sr.Microphone()

#with mic as source:
#    audio = r.listen(source)

#command = r.recognize_google(audio, language = 'pt-BR')

#print(command)
