from flask import Flask , url_for
from app import app
from flask import request
from flask import render_template
from flask.templating import render_template
import basic_sentiment_analysis 
import spell_corrector
import enchantspell
@app.route('/')
def temp():
    user = "yusuf"
    print("default")
    return render_template("Home.html",user=user)

@app.route("/register")
def register():
    return render_template("Homepage.html")
    
@app.route("/spell")
def spell():
    return render_template("Spell.html")

@app.route('/spell1/',methods =["POST"] )
def spell1():
    global user
    user = request.values.get('param')
    print(user)
    enchantoutput=enchantspell.spellenchant(user)
    #norvigoutput = spell_corrector.abcde(user)
    #test1(user)
    return render_template("spelloutput.html",sugg=enchantoutput)

@app.route("/tone")
def tone():
    return render_template("Tone.html")

@app.route('/tone1/',methods =["POST"] )
def tone1():
    global textvar
    textvar = request.values.get('param')
    toneoutput = basic_sentiment_analysis.abcd(textvar)
    return render_template("toneoutput.html",user = toneoutput)

#@app.route('/tryspell')
#def tryspell():
   # word = "'" + user +"'"
    #user2 = spell_corrector.abcde(user2)
   # return render_template("test2.html",user = user2)
@app.route("/test1")
def test1():
    #user = "yeahhhhhh "
    return render_template("test1.html",user=user)
#@app.route('/temp',methods=["POST"])

#def temp():
 #   de=request.form("param")
#    request.args.get('param')
    
#@app.route('/spell/<getting_data>')
#def spell(getting_data):
   # print(getting_data)
   # return getting_data


          
          
