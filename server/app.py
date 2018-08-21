from flask import Flask
from flask import jsonify
from flask import Flask
from flask import Request
from flask import abort
from pymongo import MongoClient

from flask import request
from flask_pymongo import PyMongo

'''
Initialize MongoDB
'''
app = Flask(__name__)
app.config.from_object('config.BaseConfig')
mongo = PyMongo(app)

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
    return ('add_resume')

@app.route('/add_view', methods=['POST'])
def add_view():
    return('add_view')

@app.route('/add_tags', methods=['POST'])
def add_view():
    return('add_view')

@app.route('/add_share', methods=['POST'])
def add_share():
    return('add_share')

@app.route('/change_validity', methods=['POST'])
def change_validity():
    return('change_validity')

@app.route('/fetch_tags', methods=['POST'])
def fetch_tags():
    return('fetch_tags')

''' delete '''

@app.route('/delete_resume', methods=['POST'])
def delete_resume():
    return ('delete_resume')

@app.route('/remove_tags', methods=['POST'])
def add_view():
    return('add_view')



'''
Get functions
'''
@app.route('/get_resume', methods=['GET'])
def get_resume():
    return('get_resume')

@app.route('/get_resume_feed', methods=['POST'])
def get_resume_feed():
    return('get_resume_feed')

if __name__ == '__main__':
    app.run(debug=True)
