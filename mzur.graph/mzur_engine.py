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

def CreateUser(self, p_name, p_age, p_gender, p_email, p_sportChosen):
	person = g.user.create(email=p_email)
	person.name = p_name
	person.age = p_age 
	person.gender = p_gender
	person.sportChosen = p_sportChosen
	person.save()
	
def ChoseSport(self,p_email,p_sportChosen):
	userID = g.user.index.lookup(email=p_email)
	sports = g.user.index.lookup(sportChosen=p_sportChosen)
	g.choses.create(userID,sports)	

 
def AssignRoutine(self, email, sportChosen):
	self.email = email
	self.sportChosen = sportChosen
	userID = g.user.index.lookup(name=self.email)
	sports = g.user.index.lookup(name=self.sportChosen)
	print "User chose sport"
