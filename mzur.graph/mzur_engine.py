from graphelements import User, Choses, Sport, Location
from bulbs.titan import Graph
import requests
import json

g = Graph()

g.add_proxy("user", User)
g.add_proxy("choses", Choses)
g.add_proxy("sport", Sport)

def CreateUser(self,name, age, gender, email,sportChosen):
	self.name = name
	self.age = age
	self.gender = gender
	self.email = email
	self.sportChosen = sportChosen
	user = g.user.create(email=self.email)
	sport = g.user.create(sportChosen = self.sportChosen)

def ChoseSport(self,email,sportChosen):
	self.email = email
	nodes = g.user.index.lookup(name=self.email)
	sports = g.user.index.lookup(name=self.sportChosen)
	vertices = list(nodes)
	vertex = vertices[0]
	choses = vertex.bothV("choses")
	for k in choses: print k.data()
 
