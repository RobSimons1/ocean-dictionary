import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import re
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'ocean_dictionary'
app.config["MONGO_URI"] =os.getenv('MONGO_URI') 

mongo = PyMongo(app)

@app.route('/')
@app.route('/show_words')
def show_words():
    return render_template("index.html", words=mongo.db.words.find())

@app.route('/get_words')
def get_words():
    return render_template("words.html", words=mongo.db.words.find().sort("word_name")) 
    #.sort to alphabetise 
 
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

@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find().sort("category_name")) 
                           # .sort added to display categories in alphabetical order  


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                           category=mongo.db.categories.find_one(
                           {'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))  

@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')    

@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))  



# GET METHOD
@app.route('/get_search')
def get_search():
    """
    Route to accept a GET request to perform
    a search
    """ 
    query = request.args.get('q') # Grab the arugments via GET request
    print(query)
    que = {'$regex': re.compile('.*{}.*'.format(query)), '$options': 'i'}
    results = mongo.db.words.find({ "word_name": que })
    # mongo.db.create_index( { name: "text", description: "text" } )
    # mongo.db.words.create_index({ "word_name": "text" })
    # total = mongo.db.words.create_index({'$text': {'$search': db_query }})
    #words = mongo.db.words.find({"word_name": { "$regex": query }}).sort("word_name",-1)
    # sort("word_name",-1) sorts into ascending alphabetical order in search.html
    #words = list(words)
    # list.sort(word_name)
    # words = mongo.db.words.sort("word_name")
    # mongo.db.words.createIndex({ category_name: "text", word_name: "text", word_definition: "text" })
    # for i in words:
    #     print(i)
    # mongo.db.words.create_index({ "$**" : "text" })
    # results = mongo.db.words.find({'$text':{'$search': query}}) # Search the db 
    #results = list(results)
    # list.sort(text)
    # results = mongo.db.words.sort("word_name")
    # for i in results:
    #     print(i)
    # print("hhhhh")
    return render_template('search.html',  query=results) # Pass the results to the view

    # categories=mongo.db.categories.sort()
                            
if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
    port=os.getenv("PORT"), debug=True)