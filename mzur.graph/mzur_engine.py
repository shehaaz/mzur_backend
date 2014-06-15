from graphelements import User, Chooses, Sport, Location, Budget, Has, LivesIn
from bulbs.titan import Graph
import requests
import json

g = Graph()

g.add_proxy("user", User)
g.add_proxy("chooses", Chooses)
g.add_proxy("has", Has)
g.add_proxy("sport", Sport)
g.add_proxy("location", Location)
g.add_proxy("lives_in", LivesIn)
g.add_proxy("budget", Budget)

def GetOrCreateUser(p_name, p_age, p_gender, p_email, p_sportList):
	# Create a new person node and pass in the properties
	person = g.user.get_or_create('email',p_email,{'email':p_email})
	person.name = p_name
	person.age = p_age 
	person.gender = p_gender
	person.sportChosen = p_sportList
	person.save()
	print "Created user %s!" %str(person.email)
	return person

def GetOrCreateSport(p_name):
	#Create a new sport and pass in the properties
	newSport = g.sport.get_or_create('name',p_name,{'name':p_name})
	newSport.save()
	return newSport
	
def ChooseSport(p_email,p_sport_name):
	#Look up the user
	person = g.user.index.get_unique('email', p_email)
	sport = g.sport.index.get_unique('name', p_sport_name)
	chooseSport =g.chooses.create(person,sport)
	#TODO
	#check if sport exists, if not, show list of available ones
	print "Sport chosen is %s!" %str(sport.name)
	return chooseSport

def GetChosenSports(p_email):
	person = g.user.index.get_unique('email', p_email)
	sports = person.bothV("chooses")
	sportList=[]
	for sport in sports: sportList.append(sport.data())
	return str(sportList)

def SetBudget(p_email, price_level):
	person = g.user.index.get_unique('email', p_email)
	budget = g.budget.create(price_level=price_level)
	hasBudget = g.has.create(person,budget)
	print "Budget set at %s!" %str(budget.price_level)
	return GetBuget(p_email)

def GetBuget(p_email):
	person = g.user.index.get_unique('email', p_email)
	budgets = person.bothV("has")
	budgetList=[]
	for budget in budgets: budgetList.append(budget.data())
	return str(budgetList)	

def SetLocation(p_email, p_location):
	person = g.user.index.get_unique('email', p_email)
	newLocation = g.location.create(location=p_location)
	setLocation = g.lives_in.create(person,newLocation)
	print "Added location %s" %str(newLocation.location)
	return setLocation

def AssignRoutine(p_email, p_sportList):
	# Look up the person
	person = g.user.index.lookup(email=p_email)
	# Look up the sports they chose
	sports = g.sport.index.lookup(name=p_sportList)
	print "User chose sport"
