from graphelements import User, Choses, Sport, Location
from mzurgraph import
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
	user = g.user.create(name=self.name)
	sport = g.user.create(sportChosen = self.sportChosen)

def ChoseSport(self,name,sportChosen):
	self.name = name
	nodes = g.user.index.lookup(name=self.name)
	sports = g.user.index.lookup(name=self.sportChosen)
	vertices = list(nodes)
	vertex = vertices[0]
	choses = vertex.bothV("choses")
	for k in choses: print k.data()
 