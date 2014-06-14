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

def CreateUser(self,name, age, gender, email, sportChosen):
	user = g.user.create()
	user.name=name, user.age=age, 
	user.gender=gender
	user.email=email
	user.sportChosen = sportChosen
	user.save()
	
def ChoseSport(self,email,sportChosen):
	self.email = email
	self.sportChosen = sportChosen
	userID = g.user.index.lookup(name=self.email)
	sports = g.user.index.lookup(name=self.sportChosen)
	g.choses.create(userID,sports)	

 
def AssignRoutine(self, email, sportChosen):
	self.email = email
	self.sportChosen = sportChosen
	userID = g.user.index.lookup(name=self.email)
	sports = g.user.index.lookup(name=self.sportChosen)
	print "User chose sport"
