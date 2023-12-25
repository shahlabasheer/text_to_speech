import pyttsx3
from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def appa():
    return render_template("index.html")

@app.route('/trasform',methods = ['POST'])
def trasform():
   if request.method == 'POST':
      input_text = request.form['name']
      gender = request.form['voice']
      text_to_speech(input_text, gender)
   return render_template("index.html")
   

def text_to_speech(text, gender):
   
    engine = pyttsx3.init()

    # Setting up voice rate
    engine.setProperty('rate', 125)

    # Setting up volume level  between 0 and 1
    engine.setProperty('volume', 0.8)

    # 0 -> male 1, female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[int(gender)].id)

    engine.say(text)
    engine.runAndWait()



if __name__ == '__main__':
   app.run()