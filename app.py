import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'ocean_dictionary'
app.config["MONGO_URI"] = 'mongodb+srv://RobSimons1:********@myfirstcluster-yyi3w.mongodb.net/ocean_dictionary?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_words')
def get_words():
    return render_template("words.html", words=mongo.db.words.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)