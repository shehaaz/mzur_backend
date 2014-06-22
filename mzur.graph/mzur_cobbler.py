# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 15:00:48 2014

@author: turbosnail9
"""

#
# Imports
#
from mzur_engine import GetOrCreateUser, GetOrCreateSport, ChooseSport, SetBudget, SetLocation, GetChosenSports
from flask import Flask, request


app = Flask(__name__)
app.config.from_object(__name__)

#http://mzur.io:5001/create_user?email=ari@mzur.io&name=ari&age=23&gender=M&sport=spartan
@app.route('/create_user')
def create_user():
	email = request.args.get('email')
	name = request.args.get('name')
	age = request.args.get('age')
	gender = request.args.get('gender')
	sport = request.args.get('sport')
	person = GetOrCreateUser(name, age, gender, email, sport)
	return "Created user %s!" %str(person.email)

@app.route('/choose_sport/<sport>/<email>')
def choose_sport(sport, email):
	expe = request.args.get('email')
	name = request.args.get('name')
	sport = GetOrCreateSport(sport)
	ChooseSport(email, sport.name)
	return email + " chooses " + str(sport.name)

@app.route('/get_sports/<email>')
def get_sports(email):
	return GetChosenSports(email)

@app.route('/set_budget/<budget>/<email>')
def set_budget(budget, email):
	return SetBudget(email, budget)

@app.route('/set_location/<location>/<email>')
def set_location(location, email):
	SetLocation(email, location)
	return email + " lives In " + location


if __name__ == '__main__':
    app.debug = True	
    app.run(host='67.207.152.182', port=5001)
