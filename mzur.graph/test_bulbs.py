#Go into the ~/python/titan folder (because that is where the people and knows models are..)

#Run these commands in the terminal.

#http://bulbflow.com/quickstart/
#It looks like we can write Gremlin code in and execute it: 
#http://stackoverflow.com/questions/16954378/bulb-flow-how-to-get-a-range-of-vertices

#stack tag: http://stackoverflow.com/questions/tagged/bulbs?page=1&sort=newest&pagesize=15



from people import Person, Knows
from bulbs.titan import Graph
import requests
import json

g = Graph()
g.add_proxy("people", Person)
g.add_proxy("knows", Knows)

james = g.people.create(name="James")
julie = g.people.create(name="Julie")

nodes = g.people.index.lookup(name="James")
vertices = list(nodes)
vertex = vertices[1]
knows = vertex.bothV("knows")
for k in knows: print k.data()


nodes = g.people.index.lookup(name="mark")
vertices = list(nodes)
vertex = vertices[0]
knows = vertex.bothV("knows")
for k in knows: print k.data()


>>> bobs  = g.people.index.lookup(name="bob")
>>> vertices = list(bobs)
>>> bob = vertices[0]


>>> g.knows.create(bob,mark)

#get james friends. Get mark and get all his friends
>>> nodes = g.people.index.lookup(name="James")
>>> vertices = list(nodes)
>>> vertex = vertices[1]
>>> knows = vertex.bothV("knows")
>>> vertices = list(knows)
>>> mark = vertices[1]
>>> knows = mark.bothV("knows")
>>> for k in knows: print k.data()

for n in nodes: print n.data()

relationship = g.knows.create(james, julie)

friends = james.outV('knows')

#json.dumps(json.loads(r.text)['results']['name'])


>>> from bulbs.rexster import Graph
>>> g = Graph()                                 # create the Graph object
>>> script = "g.V.range(start,end)"             # set a one line script
>>> params = dict(start=0, end=9)               # put function params in dict
>>> vertices = g.gremlin.query(script, params)  # execute the script in DB
>>> for vertex in vertices: print vertex.data()



from bulbs.titan import Graph
g = Graph()
script = "g.V"
vertices = g.gremlin.query(script)
for v in vertices: print v.data()


