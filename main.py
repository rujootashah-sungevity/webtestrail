from flask import Flask,render_template, jsonify
from data import models
from collections import defaultdict
import json
app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    #user = {'nickname': 'Miguel'}  # fake user
    obj=models.Models()
    projects= obj.getProjects()
    projarr=[]
    milesarr = []
    runsarr = []
    for proj in projects:
        projarr.append({'name': proj['name'], 'id': proj['id']})
        milestones=obj.getMilestonesForProject(proj['id'])
        for milestone in milestones:
            milesarr.append({'proj_id':proj['id'],'id':milestone['id'],'name':milestone['name']})

    return render_template('index.html', jsondata=milesarr)

if __name__=='__main__':
    app.run(debug=True)