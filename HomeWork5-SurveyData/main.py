#!/usr/bin/env python
from io import TextIOWrapper

import csv
import os
from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.debug import DebuggedApplication
import util
from sqlalchemy import func

basedir = os.path.abspath(os.path.dirname(__file__))

# create a Flask instance
app = Flask(__name__)
# define SQLAlchemy URL, a configuration parameter
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True





# The db object instantiated from the class SQLAlchemy represents the database and
# provides access to all the functionality of Flask-SQLAlchemy.
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


@app.route('/', methods=['GET'])
def home():
    

    group1_list,country_list1= getGroup1Records()
    
    group1_clusters=[]
    group1recordsByCountry=getGroup1RecordsCountbyCountry()
    for totalrecords in group1recordsByCountry:
        if totalrecords[1]>=10:
            kmeans_calc_group=[]
            for item in group1_list:
                if item[1] == totalrecords[0]:                    
                    kmeans_calc_group.append(item)

            group_labels = util.cluster_user_data(kmeans_calc_group)
            group_clusters = util.split_user_data(kmeans_calc_group,group_labels)
            group1_clusters.append(group_clusters)

    
    group2_list,country_list2= getGroup2Records()
    
    group2_clusters=[]
    group2recordsByCountry=getGroup2RecordsCountbyCountry()
    for totalrecords in group2recordsByCountry:
        if totalrecords[1]>=10:
            kmeans_calc_group=[]
            for item in group2_list:
                if item[1] == totalrecords[0]:                    
                    kmeans_calc_group.append(item)

            group_labels = util.cluster_user_data(kmeans_calc_group)
            group_clusters = util.split_user_data(kmeans_calc_group,group_labels)
            group2_clusters.append(group_clusters)     

    

    group3_list,country_list3= getGroup3Records()
    
    group3_clusters=[]
    group3recordsByCountry=getGroup3RecordsCountbyCountry()
    for totalrecords in group3recordsByCountry:
        if totalrecords[1]>=10:
            kmeans_calc_group=[]
            for item in group3_list:
                if item[1] == totalrecords[0]:                    
                    kmeans_calc_group.append(item)

            group_labels = util.cluster_user_data(kmeans_calc_group)
            group_clusters = util.split_user_data(kmeans_calc_group,group_labels)
            group3_clusters.append(group_clusters) 

    


    group4_list,country_list4= getGroup4Records()
    
    group4_clusters=[]
    group4recordsByCountry=getGroup4RecordsCountbyCountry()
    for totalrecords in group4recordsByCountry:
        if totalrecords[1]>=10:
            kmeans_calc_group=[]
            for item in group4_list:
                if item[1] == totalrecords[0]:                    
                    kmeans_calc_group.append(item)

            group_labels = util.cluster_user_data(kmeans_calc_group)
            group_clusters = util.split_user_data(kmeans_calc_group,group_labels)
            group4_clusters.append(group_clusters) 
        
    #records=User.query.all()
        
    
   
    #return render_template('index.html',group1=group1_list,group2=group2_list,group3=group3_list,group4=group4_list,countries=country_list) 
    #return render_template('index.html',group1=group1_list,country_list1=group1recordsByCountry,group1Kmeans=group1_clusters,group2=group2_list,country_list2=country_list2,group3=group3_list,country_list3=country_list3,group4=group4_list,country_list4=country_list4) 
    return render_template('index.html',group1=group1_list,country_list1=group1recordsByCountry,group1Kmeans=group1_clusters,group2=group2_list,country_list2=group2recordsByCountry,group2Kmeans=group2_clusters,group3=group3_list,country_list3=group3recordsByCountry,group3Kmeans=group3_clusters,group4=group4_list,country_list4=group4recordsByCountry,group4Kmeans=group4_clusters) 
    #return render_template('index.html',group1=group1_list,country_list1=country_list1,group2=group2_list,country_list2=country_list2) 
           
@app.route('/upload', methods=['POST'])
def upload_csv():
    
    """ with open('survey.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            user = User(index=row[0], country=row[1],age = row[2], fear = row[3], anxious = row[4], anger = row[5], happiness = row[6], sadness = row[7], emotionalBigImpact = row[8], reason = row[9], mostMeaning = row[10], 
            occupation = row[11], addField1 = row[12], addField2 = row[13], addField3 = row[14])
            db.session.add(user)
            db.session.commit() """
    #csv_file = request.files['survey.csv']
    #csv_file = TextIOWrapper(csv_file, encoding='utf-8')
    #app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
    #csv_reader = csv.reader('survey.csv', delimiter=',')
    #for row in csv_reader:
        #user = User(username=row[0], email=row[1])
        #db.session.add(user)
        #db.session.commit()
    #return redirect(url_for('upload_csv'))
    return render_template('index.html', log_html=User.query.all())
    

def getGroup1RecordsCountbyCountry():
   
    records=User.query.with_entities(User.country, db.func.count(User.country).label('total')).filter(User.age<=35).filter(User.gender=='Male').group_by(User.country).all();
    #records=surveyUser.query.filter(temp1).filter(temp2).all()
    list1=[]
    
    #group3_records=User.query.filter(User.age<=35).filter(User.gender=='Female').group_by(User.country).all()
    #group4_records=User.query.filter(User.age>=36).filter(User.gender=='Female').group_by(User.country).all()
    for record in records:
        list2=[]        
        list2.append(record.country)
        list2.append(record.total)
        list1.append(list2)

    return list1


def getGroup2RecordsCountbyCountry():
   
    records=User.query.with_entities(User.country, db.func.count(User.country).label('total')).filter(User.age>=36).filter(User.gender=='Male').group_by(User.country).all();
    #records=surveyUser.query.filter(temp1).filter(temp2).all()
    list1=[]
    
    #group3_records=User.query.filter(User.age<=35).filter(User.gender=='Female').group_by(User.country).all()
    #group4_records=User.query.filter(User.age>=36).filter(User.gender=='Female').group_by(User.country).all()
    for record in records:
        list2=[]        
        list2.append(record.country)
        list2.append(record.total)
        list1.append(list2)

    return list1



def getGroup3RecordsCountbyCountry():
   
    records=User.query.with_entities(User.country, db.func.count(User.country).label('total')).filter(User.age<=35).filter(User.gender=='Female').group_by(User.country).all();
    #records=surveyUser.query.filter(temp1).filter(temp2).all()
    list1=[]
    
    #group3_records=User.query.filter(User.age<=35).filter(User.gender=='Female').group_by(User.country).all()
    #group4_records=User.query.filter(User.age>=36).filter(User.gender=='Female').group_by(User.country).all()
    for record in records:
        list2=[]        
        list2.append(record.country)
        list2.append(record.total)
        list1.append(list2)

    return list1



def getGroup4RecordsCountbyCountry():
   
    records=User.query.with_entities(User.country, db.func.count(User.country).label('total')).filter(User.age>=36).filter(User.gender=='Female').group_by(User.country).all();
    #records=surveyUser.query.filter(temp1).filter(temp2).all()
    list1=[]
    
    #group3_records=User.query.filter(User.age<=35).filter(User.gender=='Female').group_by(User.country).all()
    #group4_records=User.query.filter(User.age>=36).filter(User.gender=='Female').group_by(User.country).all()
    for record in records:
        list2=[]        
        list2.append(record.country)
        list2.append(record.total)
        list1.append(list2)

    return list1



def getGroup1Records():
   
    records=User.query.filter(User.age<=35).filter(User.gender=='Male').all()
    #records=surveyUser.query.filter(temp1).filter(temp2).all()
    list1=[]
    country_list=set()
    #group3_records=User.query.filter(User.age<=35).filter(User.gender=='Female').group_by(User.country).all()
    #group4_records=User.query.filter(User.age>=36).filter(User.gender=='Female').group_by(User.country).all()
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


def getGroup2Records():
   
    records=User.query.filter(User.age>=36).filter(User.gender=='Male').all()
    #records=surveyUser.query.filter(temp1).filter(temp2).all()
    list1=[]
    country_list=set()
    #group3_records=User.query.filter(User.age<=35).filter(User.gender=='Female').group_by(User.country).all()
    #group4_records=User.query.filter(User.age>=36).filter(User.gender=='Female').group_by(User.country).all()
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



def getGroup3Records():
   
    records=User.query.filter(User.age<=35).filter(User.gender=='Female').all()
    #records=surveyUser.query.filter(temp1).filter(temp2).all()
    list1=[]
    country_list=set()
    #group3_records=User.query.filter(User.age<=35).filter(User.gender=='Female').group_by(User.country).all()
    #group4_records=User.query.filter(User.age>=36).filter(User.gender=='Female').group_by(User.country).all()
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


def getGroup4Records():
   
    records=User.query.filter(User.age>=36).filter(User.gender=='Female').all()
    #records=surveyUser.query.filter(temp1).filter(temp2).all()
    list1=[]
    country_list=set()
    #group3_records=User.query.filter(User.age<=35).filter(User.gender=='Female').group_by(User.country).all()
    #group4_records=User.query.filter(User.age>=36).filter(User.gender=='Female').group_by(User.country).all()
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



""" def getCountries:
    country_records=User.query.filter(User.age<=35).filter(User.country).distinct()

    list1=[]
   

    for country_record in country_records:             
        list1.append(country_record.country)

    return list1 """

if __name__ == '__main__':
    # get current app directory
    
    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
    app.run(debug = True, port=5287)