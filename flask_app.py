import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb+srv://Blogger:Blogger@yogacluster-kiw6r.mongodb.net/yogaBlog?retryWrites=true&w=majority"

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def getBlogs():
    user = {'username': 'Wayne'}
    return render_template('index.html', title="Home", user=user, posts=mongo.db.blogEntries.find(), tags=mongo.db.tagHeadings.find())

@app.route('/insertBlog')
def insertBlogDisplay():
    return render_template('insertBlog.html')

@app.route('/action', methods=['GET', 'POST'])
def insertBlog():
    #Insert blog article
    title = request.values.get("title")
    article_text = request.values.get("article_text")
    tag_name = request.values.get("tag_name")
    author_name = request.values.get("author_name")

    mongo.db.blogEntries.insert({"title":title, "article_text":article_text, "tag_name":tag_name, "author_name":author_name})
    return redirect("/index")

@app.route("/remove/<blog_id>")    
def remove(blog_id):    
    #Deleting a Task with various references    
    mongo.db.blogEntries.remove({"_id":ObjectId(blog_id)})    
    return redirect("/")  

@app.route('/editBlog/<blog_id>')
def editBlog(blog_id):
    theBlog = mongo.db.blogEntries.find({"_id": ObjectId(blog_id)})
    return render_template('editBlog.html', theBlog=theBlog)

@app.route("/updateBlog/<blog_id>", methods=['GET', 'POST'])    
def updateBlog(blog_id):    
    blog=mongo.db.blogEntries
    blog.update( {'_id': ObjectId(blog_id)},
    {
        'title':request.values.get("title"),
        'article_text': request.values.get("article_text"),
        'tag_name': request.values.get("tag_name"),
        'author_name': request.values.get("author_name")
    })
    return redirect("/")

@app.route("/cancel")
def cancel():
    return redirect("/")
