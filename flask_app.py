from flask import Flaskrender_template 
#rom flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://Blogger:Blogger@yogacluster-kiw6r.mongodb.net/yogaBlog?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')

#ef index():
    return render_template('index.html', title="Home", posts=mongo.db.blogEntries.find())


