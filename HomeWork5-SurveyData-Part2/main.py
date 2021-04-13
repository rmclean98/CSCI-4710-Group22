#!/usr/bin/env python
from io import TextIOWrapper

import csv
import os
from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.debug import DebuggedApplication
import util
from sqlalchemy import func
import json

basedir = os.path.abspath(os.path.dirname(__file__))

# create a Flask instance
app = Flask(__name__)
# define SQLAlchemy URL, a configuration parameter
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

if os.path.exists(os.path.join(basedir, 'data.sqlite')):
    os.remove(os.path.join(basedir, 'data.sqlite'))

db = SQLAlchemy(app)







class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    index = db.Column(db.String(80))    
    country = db.Column(db.String(120))  
    age = db.Column(db.Integer)
    gender = db.Column(db.String(120)) 
    fear = db.Column(db.Integer)
    anxious = db.Column(db.Integer)
    anger = db.Column(db.Integer)
    happiness = db.Column(db.Integer)
    sadness = db.Column(db.Integer)
    emotionalBigImpact = db.Column(db.String(500))
    reason = db.Column(db.String(1000))
    mostMeaning = db.Column(db.String(500))
    occupation = db.Column(db.String(500))
    addField1 = db.Column(db.String(500))
    addField2 = db.Column(db.String(500))
    addField3 = db.Column(db.String(500))
    

db.create_all()

app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
with open('survey.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        user = User(index=row[0], country=row[1],age = row[2],gender=row[3], fear = row[4], anxious = row[6], anger = row[6], happiness = row[7], sadness = row[8], emotionalBigImpact = row[9], reason = row[10], mostMeaning = row[11], occupation = row[12], addField1 = row[13], addField2 = row[14], addField3 = row[15])
        db.session.add(user)
        db.session.commit()    
    
    
    """ def __repr__(self):
        
        return "[{},{}]".format(self.index,self.country) """


@app.route('/details/<country>', methods=['GET'])
def surveyDetails(country):
    
    d3_toSurveyMapping={'United States of America':'USA',
    'Switzerland':'Switzerland',
    'Romania':'Romania',
    'United Kingdom':'UK',
    'Colombia':'Colombia',
    'Canada':'Canada',
    'Australia':'Australia',
    'France':'France',
    'Germany':'Germany',
    'Cyprus':'Cyprus',
    'Rwanda':'Rwanda',
    'Israel':'Israel',
    'Portugal':'Portugal',
    'Ireland':'Ireland l',
    'New Zealand':'New Zealand',
    'China':'China',
    'spain':'spain'
    }

    countryName=d3_toSurveyMapping.get(country)
    group1_list,country_list1= getGroup1Records(countryName)
    
    group1_clusters=[]
    group1recordsByCountry=getGroup1RecordsCountbyCountry(countryName)
    for totalrecords in group1recordsByCountry:
        if totalrecords[1]>10:
            kmeans_calc_group=[]
            for item in group1_list:
                if item[1] == totalrecords[0]:                    
                    kmeans_calc_group.append(item)

            group_labels = util.cluster_user_data(kmeans_calc_group)
            group_clusters = util.split_user_data(kmeans_calc_group,group_labels)
            group1_clusters.append(group_clusters)

    
    group2_list,country_list2= getGroup2Records(countryName)
    
    group2_clusters=[]
    group2recordsByCountry=getGroup2RecordsCountbyCountry(countryName)
    for totalrecords in group2recordsByCountry:
        if totalrecords[1]>10:
            kmeans_calc_group=[]
            for item in group2_list:
                if item[1] == totalrecords[0]:                    
                    kmeans_calc_group.append(item)

            group_labels = util.cluster_user_data(kmeans_calc_group)
            group_clusters = util.split_user_data(kmeans_calc_group,group_labels)
            group2_clusters.append(group_clusters)     

    

    group3_list,country_list3= getGroup3Records(countryName)
    
    group3_clusters=[]
    group3recordsByCountry=getGroup3RecordsCountbyCountry(countryName)
    for totalrecords in group3recordsByCountry:
        if totalrecords[1]>10:
            kmeans_calc_group=[]
            for item in group3_list:
                if item[1] == totalrecords[0]:                    
                    kmeans_calc_group.append(item)

            group_labels = util.cluster_user_data(kmeans_calc_group)
            group_clusters = util.split_user_data(kmeans_calc_group,group_labels)
            group3_clusters.append(group_clusters) 

    


    group4_list,country_list4= getGroup4Records(countryName)
    
    group4_clusters=[]
    group4recordsByCountry=getGroup4RecordsCountbyCountry(countryName)
    for totalrecords in group4recordsByCountry:
        if totalrecords[1]>10:
            kmeans_calc_group=[]
            for item in group4_list:
                if item[1] == totalrecords[0]:                    
                    kmeans_calc_group.append(item)

            group_labels = util.cluster_user_data(kmeans_calc_group)
            group_clusters = util.split_user_data(kmeans_calc_group,group_labels)
            group4_clusters.append(group_clusters) 
        
    
    return render_template('surveyDetails.html',group1=group1_list,country_list1=group1recordsByCountry,group1Kmeans=group1_clusters,group2=group2_list,country_list2=group2recordsByCountry,group2Kmeans=group2_clusters,group3=group3_list,country_list3=group3recordsByCountry,group3Kmeans=group3_clusters,group4=group4_list,country_list4=group4recordsByCountry,group4Kmeans=group4_clusters,countryName=countryName) 
    


@app.route('/map', methods=['GET'])
def map():
    

    country_list1= getCountriesList()

    d3_survey_mapping={'USA':'USA',
    'Switzerland':'CHE',
    'Romania':'ROU',
    'UK':'GBR',
    'Colombia':'COL',
    'Canada':'CAN',
    'Australia':'AUS',
    'France':'FRA',
    'Germany':'DEU',
    'Cyprus':'CYP',
    'Rwanda':'RWA',
    'Israel':'ISR',
    'Portugal':'PRT',
    'Ireland l':'IRL',
    'New Zealand':'NZL',
    'China':'CHN',
    'spain':'ESP'}
    
    d3_List={'USA':' United States of America',
    'CHE':'Switzerland',
    'ROU':'Romania',
    'GBR':' United Kingdom',
    'COL':'Colombia',
    'CAN':'Canada',
    'AUS':'Australia',
    'FRA':'France',
    'DEU':'Germany',
    'CYP':'Cyprus',
    'RWA':'Rwanda',
    'ISR':'Israel',
    'PRT':'Portugal',
    'IRL':' Ireland',
    'NZL':'New Zealand',
    'CHN':'China',
    'ESP':'spain'}

    countries_json = json.dumps(d3_List)       
    
    #return countries_json

    return render_template('index.html',countries_json=countries_json) 
    



@app.route('/', methods=['GET'])
def home():
   
    
    #return countries_json

    return render_template('home.html') 




def getCountriesList():
   
    records=User.query.with_entities(User.country).distinct();
    
    list1=[]
    
    
    for record in records:
        list2=[]        
        list2.append(record.country)
        
        list1.append(list2)

    return list1



    

def getGroup1RecordsCountbyCountry(country):
   
    records=User.query.with_entities(User.country, db.func.count(User.country).label('total')).filter(User.age<=35).filter(User.gender=='Male').filter(User.country==country).group_by(User.country).all();
    
    list1=[]
    
    
    for record in records:
        list2=[]        
        list2.append(record.country)
        list2.append(record.total)
        list1.append(list2)

    return list1


def getGroup2RecordsCountbyCountry(country):
   
    records=User.query.with_entities(User.country, db.func.count(User.country).label('total')).filter(User.age>=36).filter(User.gender=='Male').filter(User.country==country).group_by(User.country).all();
    
    list1=[]
    
    
    for record in records:
        list2=[]        
        list2.append(record.country)
        list2.append(record.total)
        list1.append(list2)

    return list1



def getGroup3RecordsCountbyCountry(country):
   
    records=User.query.with_entities(User.country, db.func.count(User.country).label('total')).filter(User.age<=35).filter(User.gender=='Female').filter(User.country==country).group_by(User.country).all();
    
    list1=[]
    
    
    for record in records:
        list2=[]        
        list2.append(record.country)
        list2.append(record.total)
        list1.append(list2)

    return list1



def getGroup4RecordsCountbyCountry(country):
   
    records=User.query.with_entities(User.country, db.func.count(User.country).label('total')).filter(User.age>=36).filter(User.gender=='Female').filter(User.country==country).group_by(User.country).all();
    
    list1=[]
    
    
    for record in records:
        list2=[]        
        list2.append(record.country)
        list2.append(record.total)
        list1.append(list2)

    return list1



def getGroup1Records(country):
   
    records=User.query.filter(User.age<=35).filter(User.gender=='Male').filter(User.country==country).all()
    
    list1=[]
    country_list=set()
    
    for record in records:
        list2=[]        
        list2.append(record.index)
        list2.append(record.country)
        country_list.add(record.country)
        list2.append(record.age)
        list2.append(record.gender)
        list2.append(record.fear)
        list2.append(record.anxious)
        list2.append(record.anger)
        list2.append(record.happiness)	
        list2.append(record.sadness)
        list2.append(record.emotionalBigImpact)
        list2.append(record.reason)
        list2.append(record.mostMeaning)
        list2.append(record.occupation)
        list2.append(record.addField1)
        list2.append(record.addField2)					
        list2.append(record.addField3)	
        list1.append(list2)

    return list1,country_list


def getGroup2Records(country):
   
    records=User.query.filter(User.age>=36).filter(User.gender=='Male').filter(User.country==country).all()
    
    list1=[]
    country_list=set()
    
    for record in records:
        list2=[]        
        list2.append(record.index)
        list2.append(record.country)
        country_list.add(record.country)
        list2.append(record.age)
        list2.append(record.gender)
        list2.append(record.fear)
        list2.append(record.anxious)
        list2.append(record.anger)
        list2.append(record.happiness)	
        list2.append(record.sadness)
        list2.append(record.emotionalBigImpact)
        list2.append(record.reason)
        list2.append(record.mostMeaning)
        list2.append(record.occupation)
        list2.append(record.addField1)
        list2.append(record.addField2)					
        list2.append(record.addField3)	
        list1.append(list2)

    return list1,country_list



def getGroup3Records(country):
   
    records=User.query.filter(User.age<=35).filter(User.gender=='Female').filter(User.country==country).all()
    
    list1=[]
    country_list=set()
    
    for record in records:
        list2=[]        
        list2.append(record.index)
        list2.append(record.country)
        country_list.add(record.country)
        list2.append(record.age)
        list2.append(record.gender)
        list2.append(record.fear)
        list2.append(record.anxious)
        list2.append(record.anger)
        list2.append(record.happiness)	
        list2.append(record.sadness)
        list2.append(record.emotionalBigImpact)
        list2.append(record.reason)
        list2.append(record.mostMeaning)
        list2.append(record.occupation)
        list2.append(record.addField1)
        list2.append(record.addField2)					
        list2.append(record.addField3)	
        list1.append(list2)

    return list1,country_list  


def getGroup4Records(country):
   
    records=User.query.filter(User.age>=36).filter(User.gender=='Female').filter(User.country==country).all()
    
    list1=[]
    country_list=set()
    
    for record in records:
        list2=[]        
        list2.append(record.index)
        list2.append(record.country)
        country_list.add(record.country)
        list2.append(record.age)
        list2.append(record.gender)
        list2.append(record.fear)
        list2.append(record.anxious)
        list2.append(record.anger)
        list2.append(record.happiness)	
        list2.append(record.sadness)
        list2.append(record.emotionalBigImpact)
        list2.append(record.reason)
        list2.append(record.mostMeaning)
        list2.append(record.occupation)
        list2.append(record.addField1)
        list2.append(record.addField2)					
        list2.append(record.addField3)	
        list1.append(list2)

    return list1,country_list





if __name__ == '__main__':    
    
    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
    app.run(debug = True, port=5287)