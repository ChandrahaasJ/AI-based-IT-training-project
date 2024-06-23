from flask import Flask, render_template, request, redirect, url_for,jsonify
from test import test
import json

app = Flask(__name__)
app.register_blueprint(test,url_prefix="")#url prefix is similar to app.set in express

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def nothing():
    return render_template("homepage.html")

@app.route("/compilex", methods=["GET", "POST"])
def compilex():
    return render_template("compilex.html")

@app.route("/resource-finder", methods=['GET', 'POST'])
def nitish():
    return render_template("upload.html")

@app.route("/g",methods=["GET","POST"])
def ga():
    data=request.json
    print(data)

if __name__ == "__main__":
    app.run("0.0.0.0",debug=True)
