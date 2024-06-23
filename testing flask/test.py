from flask import Flask,redirect,url_for,render_template,request
app= Flask(__name__)
@app.route('/')
def wel():
    return render_template('frontend.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    user=request.form['username']
    #f=request.form['pdf']
    with open("pdfreader.txt",'w') as fp:
        fp.write(request.form['pdf'])
    return user
    

@app.route('/sum')
def sum():
    x=3
    y=2
    ans=x+y
    if(ans<8):
        result='success'
    else:
        result='fail'
    a="8"
    return redirect(url_for(result,sum=ans))

@app.route('/success/<int:sum>')
def success(sum):
    return str(sum)

@app.route('/fail/<int:sum>')
def fail(sum):
    return "the answer is eight"+str(sum)

if __name__=='__main__':
    app.run(debug=True)