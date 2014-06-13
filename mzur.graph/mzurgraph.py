from mzurgraph import User, Choses, Sport
from bulbs.titan import Graph
import requests
import json

g = Graph()
g.add_proxy("user", User)
g.add_proxy("choses", Choses)
g.add_proxy("sport", Sport)

james = g.mzurgraph.create(name="James")
julie = g.mzurgraph.create(name="Julie")