from flask import Flask, render_template, redirect, url_for, request, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://Blogger:Blogger@yogacluster-kiw6r.mongodb.net/yogaBlog?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Wayne'}
    return render_template('index.html', title="Home", user=user, posts=mongo.db.blogEntries.find())

    




