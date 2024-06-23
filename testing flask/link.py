#import Textsum as llm
from flask import Flask,redirect,url_for,render_template,request
app= Flask(__name__)

@app.route('/',methods=["POST","GET"])
def norm():
    return "HI"
def compilex():
    return render_template('index.html')



"""
this wont work 
remove that submit button 
"""
@app.route('/compilecode',methods=["POST","GET"])
def compilecode():
    #if(request.method=="POST")
    return request.form('submit')



if(__name__=="__main__"):
    app.run(debug=True)