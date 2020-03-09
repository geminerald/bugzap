import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'bugzap'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser1@zwcluster1-znjzd.mongodb.net/bugzap?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_bugs')
def get_bugs():
    return render_template("bugs.html", bugs=mongo.db.bug.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)