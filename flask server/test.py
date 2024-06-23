from flask import Flask, Blueprint

test=Blueprint("test",__name__)


@test.route("/go", methods=["GET","POST"])
def noi():
    return "HI"


