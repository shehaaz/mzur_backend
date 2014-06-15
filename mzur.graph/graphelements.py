#mzurgraph.py
from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, List, DateTime
from bulbs.utils import current_datetime

class User(Node):
	
	element_type = "user"

	name = String(nullable=True)
	age = Integer()
	gender = String(nullable=True)
	email = String(nullable=False)
	sportChosen = List()
	isAvailable = List()

class Sport(Node):
	element_type = "sport"
	
	name = String(nullable=False)

class Budget(Node):
	element_type = "budget"

	price_level = Integer()

class Location(Node):
	element_type = "location"

	location = String(nullable=False)



class Assigns(Node):
	element_type = "assigns"

	created = DateTime(default=current_datetime, nullable=False)

class Chooses(Relationship):
	label = "chooses"

	created = DateTime(default=current_datetime, nullable=False)
	#TODO: add properties to chooses
	# experience_level = Integer()
	# fitness_level = Integer()
	# budget = personal budget

class Has(Relationship):
	label = "has"

	created = DateTime(default=current_datetime, nullable=False)

class LivesIn(Relationship):
	label = "lives_in"

	created = DateTime(default=current_datetime, nullable=False)
