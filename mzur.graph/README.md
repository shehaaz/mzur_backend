#MZUR GRAPH

This is the MZUR graph DB code base. 

##Graph Elements
The script `graphelements.py` contains the definitions all the graph elements (nodes and relationships). If you want to make a new element, add it to this script. Make sure to import it in `mzur_engine.py` if you want to use it!

##MZUR Engine

##MZUR Cobbler
This is the web service that contains all the endpoints for the MZUR Engine. You can create new endpoints here. As a usage example, you can create a new user named *ari*, give him an email address, age and gender, and assign a sport to him as follows: 
`http://mzur.io:5001/create_user?email=ari@mzur.io&name=ari&age=23&gender=M&sport=spartan`

