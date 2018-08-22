from flask import Flask
from flask import jsonify
from flask import Flask
from Flask import json
from flask import Request
from flask import abort
from pymongo import MongoClient

from flask import request
from flask_pymongo import PyMongo
import httplib
import bson
import datetime


'''
Constants
'''
DEFAULT_VALUE = 0
'''
Initialize MongoDB
'''
app = Flask(__name__)
app.config.from_object('config.BaseConfig')
mongo = PyMongo(app)
db = mongo.db
'''
404s
'''
@app.route('/')
def index():
    abort(404)

'''
Post functions
'''

''' add '''

@app.route('/add_resume', methods=['POST'])
def add_resume():
    url = request.args.get('url')
    exists(url)
    resume = dict()
    resume['tags'] = []
    resume['views'] = DEFAULT_VALUE
    resume['shares'] = DEFAULT_VALUE
    resume['url'] = url
    resume['valid'] = url_exists(url)
    resume['time'] = datetime.datetime.today().timestamp()
    post_status = db.resume.insert(resume)
    return (post_status_valid(post_status))

@app.route('/add_view', methods=['POST'])
def add_view():
    id = requests.args.get('id')
    exists(id)
    post_status = db.resume.update(
        {_id: generate_object_id(id)},
        { $inc: { views: 1 } }
    )
    return(post_status_valid(post_status))

@app.route('/add_tags', methods=['POST'])
def add_tags():
    id = requests.args.get('id')
    tags = requests.args.get('tags')
    exists(id)
    exists(tags)
    tags_to_json = json.loads(tags)
    post_status = db.resume.update(
        {_id: generate_object_id(id)},
        { $addToSet: { tags: { $each: tags_to_json } } }
    )
    return(post_status_valid(post_status))

@app.route('/add_share', methods=['POST'])
def add_share():
    id = requests.args.get('id')
    exists(id)
    post_status = db.resume.update(
        {_id: generate_object_id(id)},
        { $inc: { shares: 1 } }
    )
    return(post_status_valid(post_status))

@app.route('/change_validity', methods=['POST'])
def change_validity():
    id = requests.args.get('id')
    validity = requests.args.get('validity')
    exists(id)
    exists(validity)
    post_status = db.resume.update(
        {_id: generate_object_id(id)},
        { valid: validity }
    )
    return(post_status_valid(post_status))

''' delete '''

@app.route('/delete_resume', methods=['POST'])
def delete_resume():
    id = requests.args.get('id')
    exists(id)
    post_status = db.resume.remove(
        {_id: generate_object_id(id)},
    )
    return(post_status_valid(post_status))

@app.route('/remove_tags', methods=['POST'])
def remove_tags():
    id = requests.args.get('id')
    exists(id)
    post_status = db.resume.update(
        {_id: generate_object_id(id)},
        { tags: [] }
    )
    return(post_status_valid(post_status))



'''
Get functions
'''
@app.route('/get_resume', methods=['GET'])
def get_resume():
    id = requests.args.get('id')
    exists(id)
    cursor = db.resume.find(
        {_id: generate_object_id(id)},
    )
    return(get_response_for_object(cursor))

@app.route('/get_resume_feed', methods=['POST'])
def get_resume_feed():
    page = requests.args.get('page')
    exists(page)
    results_skip = 15 * page
    cursor = db.resume.find().sort( { time: 1 } ).skip(results_skip).limit(15)
    return(get_response_for_object(cursor))


'''
Error Messages & Helpers
'''
def exists(obj):
    data = {
        'message': 'URL does not exist!'
    }
    if obj is None or obj is '':
        return (jsonify(data))

def url_exists(url):
    c = httplib.HTTPConnection(url)
    c.request("HEAD", '')
    if c.getresponse().status is not 200:
        return(False)
    return(True)

def post_status_valid(status):
    data = {
        'failed': 'Creation failed!',
        'success': 'Creation succeeded!'
    }
    if ("writeConcernError" in status.keys()):
        return (jsonify(data['failed']))
    return (jsonify(data['success']))


def generate_object_id(id):
    return (bson.objectid.ObjectId(id))

def get_response_for_object(cursor):
    return(jsonify(bson.json_util.dumps(cursor)))

if __name__ == '__main__':
    app.run(debug=True)
