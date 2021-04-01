#!/usr/bin/env python
from io import TextIOWrapper
import csv
import os
from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.debug import DebuggedApplication
import util

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
    
    
    
    
    
    """ def __repr__(self):
        
        return "[{},{}]".format(self.index,self.country) """


@app.route('/', methods=['GET'])
def home():
    
        
    app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
    """  with open('survey.csv', 'r') as file:
       csv_reader = csv.reader(file, delimiter=',')
       for row in csv_reader:
           user = User(index=row[0], country=row[1],age = row[2],gender=row[3], fear = row[4], anxious = row[6], anger = row[6], happiness = row[7], sadness = row[8], emotionalBigImpact = row[9], reason = row[10], mostMeaning = row[11], occupation = row[12], addField1 = row[13], addField2 = row[14], addField3 = row[15])
           db.session.add(user)
           db.session.commit()  """
    
    
    # response="""<table class="table" id="table" >
    # <caption>Survey Statistics</caption>
    
      
    #country_list=getCountries()
    group1_list,country_list1= getGroup1Records()
    group2_list,country_list2= getGroup2Records()
    group3_list,country_list3= getGroup3Records()
    group4_list,country_list4= getGroup4Records()
    
    #records=User.query.all()
        

    #record_dict = {	'user_data':records}

    

      
   			
						
    # response +='</table>'
           #"""
        
        
    #response="""
            #<form method='post' action='/upload' enctype='multipart/form-data'>
              #Upload a csv file: <input type='file' name='file'>
              #<input type='submit' value='Upload'>
            #</form>
           #"""
    #return render_template('index.html', log_html=response)
    #render_template('index.html',response=records)
    
    #res= """
            #<form method='post' action='/upload' enctype='multipart/form-data'>
              #Upload a csv file: <input type='file' name='file'>
              #<input type='submit' value='Upload'>
            #</form>
           #"""
    #return res
    #return render_template('index.html',group1=group1_list,group2=group2_list,group3=group3_list,group4=group4_list,countries=country_list) 
    return render_template('index.html',group1=group1_list,country_list1=country_list1,group2=group2_list,country_list2=country_list2,group3=group3_list,country_list3=country_list3,group4=group4_list,country_list4=country_list4) 
           
@app.route('/upload', methods=['POST'])
def upload_csv():
    
    with open('survey.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            user = User(index=row[0], country=row[1],age = row[2], fear = row[3], anxious = row[4], anger = row[5], happiness = row[6], sadness = row[7], emotionalBigImpact = row[8], reason = row[9], mostMeaning = row[10], 
            occupation = row[11], addField1 = row[12], addField2 = row[13], addField3 = row[14])
            db.session.add(user)
            db.session.commit()
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
    db.create_all()
    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
    app.run(debug = True, port=5287)