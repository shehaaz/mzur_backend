#!/usr/bin/env python

from flask import Flask, request, render_template, url_for, redirect, session, g
from humanapi import get_authorize_url, get_auth_session, recreate_session
from flask_googleauth import GoogleAuth
from cassandra.cluster import Cluster
import json
import settings
from humandriver import HumanAPI, Profile, Human, Periodical, Activity, Sleep

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY
app.secret_key = "AIzaSyBKvw7D63hSx26JhAi6YressQi86r_f368"

cluster = Cluster()
cass = cluster.connect()
cass.set_keyspace('mzur')
print "connected to keyspace"

# Setup Google Federated Auth
auth = GoogleAuth(app)
auth_session = None

@app.route('/')
@auth.required
def index():
    #If user has a token
    query = "SELECT * FROM users WHERE email=%s"
    result = cass.execute_async(query,[str(g.user['email'])])
    row = result.result()
    
    #New User sent to connect devices
    if True:
        return redirect(url_for('humanapi_authorize'))
    else:
        value = row[0]
        token = str(value.humantoken)
        #Already existing user recreates session
        return redirect(url_for('humanapi_recreate_session', token=token))

#authorization call to HUMAN API
@app.route('/humanapi/authorize')
def humanapi_authorize():
    redirect_uri = url_for('humanapi_callback', _external=True)
    authorize_url = get_authorize_url(redirect_uri)
    return redirect(authorize_url)

#CallBACK endpoint for HUMAN API
@app.route('/humanapi/callback')
def humanapi_callback():
    # Get code from response
    code = request.args.get('code')
    if not code:
        return 'Error: code parameter must be provided in oauth2 callback', 400

    # Get an authorized session with HumanAPI
    global auth_session
    auth_session = get_auth_session(code)

    #save access token in C*
    query = "INSERT INTO users (email,humantoken) VALUES(%s,%s)"
    cass.execute_async(query,[str(g.user['email']),str(auth_session.access_token)])
    
    token = str(auth_session.access_token)

    # Redirect to profile page
    return redirect(url_for('profile'))

#recreate user session
@app.route('/token/<token>')
def humanapi_recreate_session(token):
    global auth_session   
    auth_session = recreate_session(token)
    humanApi = HumanAPI(auth_session.access_token,True)
    return redirect(url_for('profile'))

#date is YYYY-MM-DD form
@app.route('/sleep/<date>/')
def sleep(date):
    if auth_session == None:
        return redirect(url_for('index'))
    else:    
        humanApi = HumanAPI(auth_session.access_token,True)
        periodical = Sleep(humanApi)
        return json.dumps(periodical.summary(date))

#date is YYYY-MM-DD form
@app.route('/activity/<date>/')
def activity_summary(date):
    if auth_session == None:
        return redirect(url_for('index'))
    else: 
        humanApi = HumanAPI(auth_session.access_token,True)
        periodical = Activity(humanApi)
        return json.dumps(periodical.summary(date))


@app.route('/profile/')
def profile():
    if auth_session == None:
        return redirect(url_for('index'))
    else: 
        humanApi = HumanAPI(auth_session.access_token,True)
        return json.dumps(Profile(humanApi).get())
       

if __name__ == '__main__':
    app.debug = True	
    app.run(host='67.207.152.182')
