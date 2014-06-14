#mzurgraph.py
from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime

class User(Node):
	
	element_type = "user"

	name = String(nullable=False)
	age = Integer()
	gender = String(nullable=False)
	email = String(nullable=False)
	sportChosen = List()
	isAvailable = List()

class Sport(Node):
	element_type = "sport"

	experience_level = Integer()
	fitness_level = Integer()

class Budget(Node):
	element_type = "budget"

	price_level = Integer()

class Location(Node):
	element_type = "budget"

	location = Double()



class Assigns(Node):
	element_type = "assigns"

	created = DateTime(default=current_datetime, nullable=False)

class Choses(Relationship):
	label = "choses"

	created = DateTime(default=current_datetime, nullable=False)

class Has(Relationship):
	label = "has"

	created = DateTime(default=current_datetime, nullable=False)
