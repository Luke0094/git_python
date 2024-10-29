from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from service import readData, showData, createData, updateData, deleteData

# import json

app = Flask(__name__)

# obj = { "subs": ["orsociro@gmail.com", "mattia.folcarelli@gmail.com", "ernesto@gmail.com"]}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/sub", methods=["GET"])
def index_subs():
    # return json.dumps();
    data = readData()
    return jsonify(data)


@app.route("/sub/<int:id>", methods=["GET"])
def show_subs(id):
    # return jsonify(obj['subs'][int(id)])
    return showData(id)


@app.route("/sub", methods=["POST"])
def create_subs():
    newSub = request.form["sub"]
    # obj["subs"].append(newSub)
    createData("\n" + newSub , "a")
    return jsonify({"data": newSub})


@app.route("/sub", methods=["PUT"])
def update_subs():
    newSub = request.json["sub"]
    id = request.json["index"]
    updateData(id, newSub)
    return jsonify({"data": newSub})


@app.route("/sub/<int:id>", methods=["DELETE"])
def delete_subs(id):
    element = deleteData(id)
    return jsonify({"data": element})
