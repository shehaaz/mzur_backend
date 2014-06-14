from graphelements import User, Choses, Sport, Location, Budget, Has
from bulbs.titan import Graph
import requests
import json

g = Graph()

g.add_proxy("user", User)
g.add_proxy("choses", Choses)
g.add_proxy("has", Has)
g.add_proxy("sport", Sport)
g.add_proxy("location", Location)
g.add_proxy("budget", Budget)

def CreateUser(p_name, p_age, p_gender, p_email, p_sportList):
	# Create a new person node and pass in the properties
	if g.user.index.lookup(email=p_email)==null:
		person = g.user.create(email=p_email)
		person.name = p_name
		person.age = p_age 
		person.gender = p_gender
		person.sportChosen = p_sportList
		person.save()

def CreateSport(p_name, p_experience_level, p_fitness_level):
	#Create a new sport and pass in the properties
	if g.sport.index.lookup(name=p_name)==null:
		newSport = g.sport.create(p_name)
		newSport.experience_level = p_experience_level
		newSport.fitness_level = p_fitness_level
		newSport.save()
	
def ChoseSport(self,p_email,p_sport):
	#Look up the user
	person = g.user.index.lookup(email=p_email)
	#Look up the sport they chose
	sportSelected = g.sport.index.lookup(name=p_sport)
	#Add that sport to the list of all chosen sports
	person.sportChosen.append(p_sport)
	#Update the user node with the new sport list
	g.user.update(person, person.sport)
	#Create an edge between person and the sport they chose
	g.choses.create(person,sportSelected)	

 
def AssignRoutine(p_email, p_sportList):
	# Look up the person
	person = g.user.index.lookup(email=p_email)
	# Look up the sports they chose
	sports = g.sport.index.lookup(name=p_sportList)
	print "User chose sport"
