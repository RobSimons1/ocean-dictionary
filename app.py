import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'ocean_dictionary'
app.config["MONGO_URI"] =os.getenv('MONGO_URI') 

mongo = PyMongo(app)


  
@app.route('/get_words')
def get_words():
    return render_template("words.html", words=mongo.db.words.find())

 
@app.route('/add_word')
def add_word():
    return render_template('addword.html',
    categories=mongo.db.categories.find())  

   
@app.route('/insert_word', methods=['POST'])
def insert_word():
    words = mongo.db.words
    words.insert_one(request.form.to_dict())
    return redirect(url_for('get_words'))  

      
@app.route('/edit_word/<word_id>')
def edit_word(word_id):
    the_word =  mongo.db.words.find_one({"_id": ObjectId(word_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editword.html', word=the_word, categories=all_categories)   

@app.route('/update_word/<word_id>', methods=["POST"])
def update_word(word_id):
    words = mongo.db.words
    words.update( {'_id': ObjectId(word_id)},
    {
        'category_name':request.form.get('category_name'),
        'word_name':request.form.get('word_name'),
        'word_definition': request.form.get('word_definition')
        
    })
    return redirect(url_for('get_words'))

@app.route('/delete_word/<word_id>')
def delete_word(word_id):
    mongo.db.words.remove({'_id': ObjectId(word_id)})
    return redirect(url_for('get_words')) 

@app.route('/')
@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())          
                            
if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
    port=os.getenv("PORT"))