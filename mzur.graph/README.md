#Quickstart

This is the MZUR graph DB code base. To add a new feature to this graph, you can use the following procedure:

1. Create new graph elements (nodes, relationships) in `graphelements.py`
2. Import the elements into `mzur_engine.py` and create a method to handle the new functionality. (eg. GetFavouriteSport)
3. Add an endpoint in `mzur_cobbler.py` so that the app that allows the app access to the backend.

##Graph Elements
The script `graphelements.py` contains the definitions all the graph elements (nodes and relationships). If you want to make a new element, add it to this script. Make sure to import it in `mzur_engine.py` if you want to use it!

##MZUR Engine
This script imports the building blocks defined in `graphelements.py` and handles all the backend logic eg. getting or creating a new user, assigning a sport to a user, setting a budget etc.

##MZUR Cobbler
This is the web service that contains all the endpoints for the MZUR Engine. You can create new endpoints here. As a usage example, you can create a new user named *ari*, give him an email address, age and gender, and assign a sport to him as follows: 
`http://mzur.io:5001/create_user?email=ari@mzur.io&name=ari&age=23&gender=M&sport=spartan`

