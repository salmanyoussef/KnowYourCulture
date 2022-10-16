from wsgiref import headers
from flask import Blueprint, render_template, redirect, url_for, request, Flask
from bson.objectid import ObjectId
from bson.json_util import dumps
from todoapp.extensions import mongo
from flask_cors import CORS, cross_origin

main = Blueprint('main', __name__)
app = Flask(__name__)
app.config['CORS_HEADER'] = 'Content-Type'

cors = CORS(app, resources={r"/getPost": {"origins": 'http://localhost:5000'}})

# @main.route('/')
# def index():
#   todos_collection = mongo.db.todos
#   todos = todos_collection.find()
#   return render_template('index.html', todos=todos)

# @main.route('/add_todo', methods=['POST'])
# def add_todo():
#   todos_collection = mongo.db.todos
#   todo_item = request.form.get('add-todo')
#   todos_collection.insert_one({'text': todo_item, 'complete': False})
#   return redirect(url_for('main.index'))

# @main.route('/complete_todo/<oid>')
# def complete_todo(oid):
#   todos_collection = mongo.db.todos
#   todo_item = todos_collection.find_one({'_id': ObjectId(oid)})
#   todo_item['complete'] = True
#   todos_collection.replace_one({'_id' : ObjectId(oid)}, todo_item)
#   return redirect(url_for('main.index'))

# @main.route('/delete_completed')
# def delete_completed():
#   todos_collection = mongo.db.todos
#   todos_collection.delete_many({'complete' : True})
#   return redirect(url_for('main.index'))

# @main.route('/delete_all')
# def delete_all():
#   todos_collection = mongo.db.todos
#   todos_collection.delete_many({})
#   return redirect(url_for('main.index'))

@main.route('/getPost/<country>')
def getPost(country):
  posts_collection = mongo.db.todos
  posts = posts_collection.find({'country' : country})
  returnable = list(posts)
  JSONReturnable = dumps(returnable)
  return JSONReturnable

@main.route('/addPost/', methods=['POST'])
def addPost():
  country = request.args.get('country')
  title = request.args.get('title')
  desc = request.args.get('desc')
  if(country == None or title == None or desc == None):
    return '', 400
  
  posts_collection = mongo.db.todos
  try:
    posts_collection.insert_one({'country': country, 'title': title, 'desc': desc})
    return '',200
  except:
    return '',404

@main.route('/deletePost/<oid>', methods=['DELETE'])
def complete_todo(oid):
  posts_collection = mongo.db.todos
  try:
    posts_collection.delete_many({'_id' : ObjectId(oid)})
    return '',200
  except:
    return '',404