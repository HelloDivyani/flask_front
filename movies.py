#!/usr/bin/env python
import os
import csv
#import first_borda
import subprocess
import shlex
from json import dumps
from flask import Flask, g, Response, request

from neo4j.v1 import GraphDatabase, basic_auth

app = Flask(__name__, static_url_path='/static/')

password = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver('bolt://localhost',auth=basic_auth("neo4j", password))

def get_db():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'neo4j_db'):
        g.neo4j_db.close()

@app.route("/")
def get_index():
    return app.send_static_file('index.html')


def serialize_data(pol):
    return {
        'Screen_Name':pol['Screen_Name'],
        'Name': pol['Name'],
        'Image': pol['Image'],
        'Followers': pol['Followers'],
        'Location': pol['Location']
        }
     

@app.route("/search",methods=['POST', 'GET'])
def get_search():
    #print("Search function")
    if request.method=='POST':
        #print("here post")
        features =request.form.getlist('check')
        option = request.form['optradio']
        loc=request.form['location']
        #print(features,option,loc)
        #print("plz")

        if option=='1':
            op=[['1.csv']]
        elif option=='2':
            op=[['2.csv']]
        elif option=='3':
            op=[['3.csv']]
        elif option=='4':
            op=[['4.csv']]
        elif option=='5':
            op=[['5.csv']]
        elif option=='6':
            op=[['6'.csv]]
        elif option=='7':
            op=[['7.csv']]

        with open('process3.csv', 'w') as csvfile: 
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerows(op)
            csvwriter.writerows(features)
        csvfile.close();
        print("Before subprocess")
        #execfile("first_borda.py")
        subprocess.call(['./myshell.sh'])
        #print("SCript")
        db = get_db()
        results = db.run("MATCH (u:User{Screen_Name:'narendramodi'})RETURN u")
        #for r in results:
        #   print(r)
        #print("Here")
        return Response(dumps([serialize_data(record['u']) for record in results]),
                    mimetype="application/json")
        #return render_template("index.html",result = dumps([serialize_data(record['u']) for record in results]),mimetype="application/json")
        #return render_template("index.html")
    else:
        print("error here")
        return "error"

       

        
if __name__ == '__main__':
    app.run(port=8080)
