from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
from LLMs import nitish as nt
from LLMs import nip 
from LLMs import ananya as an
app = Flask(__name__)
app.register_blueprint(nip,url_prefix="")


@app.route("/res-finder",methods=["POST"])
def LLMs():
    getpdf=request.json
    pdf=getpdf["pdf"]
    x=nt.final_task(pdf)
    return jsonify({"output":x})




if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)
