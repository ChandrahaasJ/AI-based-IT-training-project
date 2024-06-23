from flask import Flask,render_template,redirect,url_for,request
app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def welc():
    if request.method=="POST":
        print(request.data)
        return({"name":"chna","age":19,"sex":"male"})
    elif request.method=="GET":
        return render_template("index.html")


@app.route('/upload',methods=["POST","GET"])
def upload():
    return render_template('frontend.html')

@app.route('/submit',methods=["POST","GET"])
def submit():
    request.form()



if(__name__=="__main__"):
    app.run(debug=True)