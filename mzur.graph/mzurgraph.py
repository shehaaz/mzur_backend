import os
import jpype
import requests
import json
from mzur_engine import CreateUser
from flask import Flask, g


# configuration
DATABASE = 'graphdatabase'
DEBUG = True
SECRET_KEY = 'boo'
USERNAME = 'mzur'
PASSWORD = 'bla'
ADMIN = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/user/<name>')
def user(name):
	user = CreateUser(name=name.toString())

@app.route('/choses/<sport>')
def choses(sport):
    return 'User chose, {0}!'.format(sport)

@app.route('/has/<budget>')
def has(budget):
	return 'User has budget, {0}!'.format(budget)

