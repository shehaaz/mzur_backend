# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 15:00:48 2014

@author: turbosnail9
"""

#
# Imports
#
from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, List, DateTime
from bulbs.utils import current_datetime

#
# Node Classes
#
class User(Node):
	"""A user node"""
	#
	#Class members
	#
	element_type = "user"
	
	#
	#Node properties
	#
	name = String(nullable=True)
	age = Integer()
	gender = String(nullable=True)
	email = String(nullable=False)
	sportChosen = List()
	isAvailable = List()

class Sport(Node):
	"""A sport node"""
	#
	#Class members
	#
	element_type = "sport"
	
	#
	#Node properties
	#
	name = String(nullable=False)

class Budget(Node):
	"""A Budget node"""
	
	#
	#Class members
	#
	element_type = "budget"
	
	#
	#Node properties
	#
	price_level = Integer()

class Location(Node):
	"""A location node"""
	
	#
	#Class members
	#
	element_type = "location"
	
	#
	#Node properties
	#
	location = String(nullable=False)

#
#Relationship Classes
#
class Assigns(Relationship):
	"""Assigns relationship"""
	
	#
	#Class members
	#
	element_type = "assigns"
	
	#
	#Relationship properties
	#
	created = DateTime(default=current_datetime, nullable=False)

class Chooses(Relationship):
	"""Chooses relationship"""
	
	#
	#Class members
	#
	label = "chooses"
	
	#
	#Relationship properties
	#
	created = DateTime(default=current_datetime, nullable=False)
	#TODO: add properties to chooses
	# experience_level = Integer()
	# fitness_level = Integer()
	# budget = personal budget

class Has(Relationship):
	"""Has relationship"""
	
	#
	#Class members
	#
	label = "has"
	
	#
	#Relationship properties
	#
	created = DateTime(default=current_datetime, nullable=False)

class LivesIn(Relationship):
	"""LivesIn relationship"""
	
	#
	#Class members
	#
	label = "lives_in"
	
	#
	#Relationship properties
	#
	created = DateTime(default=current_datetime, nullable=False)
