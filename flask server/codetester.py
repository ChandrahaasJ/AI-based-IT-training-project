from flask import Flask,render_template,redirect,request
from LLMs import pdfext
import PyPDF2
app=Flask(__name__)

@app.route("/",methods=['get','post'])
def welcome():
    return render_template("testupload.html")

@app.route("/upload",methods=['get','post'])
def upload():
    pdfpath=request.files['pdf']
    pdfext.pdftotext(pdfpath)
    return "done"


if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=9900,debug=True)