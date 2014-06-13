#mzurgraph.py

from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime

class User(Node):
	element_type = "user"

    name = String(nullable=False)
    age = Integer()
    gender = String(nullable=False)

class Sport(Node):
	element_type = "sport"

	experience_level = Integer()
	fitness_level = Integer()

class Budget(Node):
	element_type = "budget"

	price_level = Integer()

class Season(Node):
	element_type = "season"

	season = Integer()

class TrendingAcitivity(Node):
	element_type = "trendingActivity"

	name = String(nullable=False)

class Feedback(Node):
	element_type = "feedback"

	response = String(nullable=False)

class Choses(Relationship):
	label = "choses"

	created = DateTime(default=current_datetime, nullable=False)

class HasValue(Relationship):
	label = "hasValue"

	created = DateTime(default=current_datetime, nullable=False)

class HasName(Relationship):
	label = "hasName"

	created = DateTime(default=current_datetime, nullable=False)