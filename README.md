#The MZUR Backend Service
============

Setup Environment
---

Start Cassandra: 
`$ cassandra -f`

Start Titan
`$TITAN/bin/titan.sh start`

Status Titan
`$TITAN/bin/titan.sh status`

`pip install requirements.txt`


--
mzur.core
--
To start Flask Server
`$ python app.py`

Navigate to:
`http://mzur.io:5000/`


--
mzur.graph
--

This is where the graph database resides. It's written in Python and uses the Tinkerpop Stack and Titan Graph DB

#TODO

Implement GraphDB
Write the documentation on using it
Create Tests for DB
Set up Travis CI

