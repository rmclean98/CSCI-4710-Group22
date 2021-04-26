#!/usr/bin/env python
from io import TextIOWrapper
import csv
import os
import json
from flask import Flask, request, redirect, url_for, render_template, session, jsonify,make_response,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
#from model.User import User
from werkzeug.debug import DebuggedApplication
from datetime import datetime
#import util

basedir = os.path.abspath(os.path.dirname(__file__))

# create a Flask instance
app = Flask(__name__)
# define SQLAlchemy URL, a configuration parameter
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'Classifieds.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
#from model.Register import db2
#db2.create_all()
#from model.UserDetails import db1
from model.Model import db1
from model.Model import AdDetails
from model.Model import UserDetails
from model.Model import Register
from model.Model import AdFiles
from model.Model import AdsList
db1.create_all()



@app.route('/classifieds/signup/', methods=['GET','POST'])
def signup():


    if  request.method =='GET':

        return render_template('signup.html')


    if  request.method =='POST':

        createUser(request)

        confirmMessage1='Hurrah, your registration is completed successfully!!!'
        confirmMessage2='Please login with your user credentials from the homepage.'
        redirection='/classifieds'
        return render_template('confirmation.html',confirmMessage1=confirmMessage1,confirmMessage2=confirmMessage2,redirection=redirection)
        #return redirect(url_for('home'))

            #resp =make_response(render_template('index.html',recentAdslist=recentAdslist))



    #return resp

@app.route('/classifieds/updateprofile', methods=['POST'])
def updateProfile():





    if  request.method =='POST':

        updateUser(request)

        confirmMessage1='Hurrah, your profile is updated successfully!!!'
        confirmMessage2='Please verify if your profile information is displayed correctly the homepage.'
        redirection='/classifieds'
        return render_template('confirmation.html',confirmMessage1=confirmMessage1,confirmMessage2=confirmMessage2,redirection=redirection)
        #return redirect(url_for('home'))

            #resp =make_response(render_template('index.html',recentAdslist=recentAdslist))



    #return resp


@app.route('/classifieds/login/', methods=['POST'])
def login():



    data = request.json
    email = data["username"]
    password = data["password"]

    loginValidation={}



    checkloginResults=CheckLogin(email,password)


    if len(checkloginResults)>0:
        loginValidation['loginStatus']='Successful'
        loginValidation['userDetails']=checkloginResults
        session['username']=email
        #recentAdslist=getRecentAds()
    else:
        loginValidation['loginStatus']='Failure'
        #recentAdslist=[]


    return redirect(url_for('home'))




@app.route('/classifieds/logout/', methods=['GET'])
def logout():



    if 'username' not in session:
        session['username']='Guest'
        recentAdslist=getRecentAds()
        resp =make_response(render_template('index.html',session_variable=str(session['username']),recentAdsList=recentAdslist))
        resp.set_cookie('Authenticated', 'No')

    elif session['username']=='Guest':
        recentAdslist=getRecentAds()
        resp =make_response(render_template('index.html',session_variable=str(session['username']),recentAdsList=recentAdslist))
        resp.set_cookie('Authenticated', 'No')

    else:
        session['username']='Guest'
        recentAdslist=getRecentAds()
        #resp =make_response(render_template('index.html',session_variable=str(session['username']),recentAdsList=recentAdslist))

        resp =redirect(url_for('home'))
        resp.set_cookie('Authenticated', 'No')




    return resp




@app.route('/classifieds', methods=['GET'])
def home():


    if 'username' not in session:
        session['username']='Guest'
        recentAdslist=getRecentAds()
        resp =make_response(render_template('index.html',session_variable=str(session['username']),recentAdsList=recentAdslist))
        resp.set_cookie('Authenticated', 'No')

    elif session['username']=='Guest':
        recentAdslist=getRecentAds()
        resp =make_response(render_template('index.html',session_variable=str(session['username']),recentAdsList=recentAdslist))
        resp.set_cookie('Authenticated', 'No')

    else:
        recentAdslist=getRecentAds()
        myAdsList=getMyAds(session['username'])
        profileInfo=getUserDetails(session['username'])
        resp =make_response(render_template('home.html',session_variable=str(session['username']),recentAdsList=recentAdslist,myAdsList=myAdsList,profileInfo=profileInfo))
        resp.set_cookie('Authenticated', 'Yes')

    return resp
    #return render_template('index.html',group1=group1_list,country_list1=country_list1,group2=group2_list,country_list2=country_list2)



@app.route('/classifieds/adId/<adId>', methods=['GET'])
def viewAd(adId):

    adDetailRecord,userRecord,adFilesList=getAdDetails(adId)

    return render_template('viewad.html',adDetailRecord=adDetailRecord,userRecord=userRecord,adFilesList=adFilesList)


@app.route('/classifieds/edit/adId/<adId>', methods=['GET', 'POST'])
def editAd(adId):
	
	print(adId)
	adDetailRecord,userRecord,adFilesList=getAdDetails(adId)
	adRecords = AdDetails.query.filter(AdDetails.adId==adId).all()
    
	print(adRecords)
	print(request.form.get('title'))
    
	for record in adRecords:
		print(record)
		record.adTitle = request.form.get('title')
		record.adDescription = request.form.get('desc')
		#record.adType = request.form.get('')
		record.expectedPrice = request.form.get('price')
		record.payFrequency = request.form.get('freq')
		record.postedDate = request.form.get('date')
		db1.session.commit()

		
	return render_template('editad.html',adDetailRecord=adDetailRecord,userRecord=userRecord,adFilesList=adFilesList)


@app.route('/classifieds/delete/adId/<adId>', methods=['GET', 'POST'])
def deleteAd(adId):

    adDetailRecord,userRecord,adFilesList=getAdDetails(adId)
    x = len(adDetailRecord) - 1
    db1.session.delete(adDetailRecord[x])

    return render_template('/classifieds')



@app.route('/classifieds/uploads/<filename>')
def assets(filename):
  # Add custom handling here.
  # Send a file download response.
  assets_folder = os.path.join('', 'uploads')
  return send_from_directory(assets_folder, filename)


@app.route('/classifieds/static/js/<filename>')
def staticAssets(filename):
  # Add custom handling here.
  # Send a file download response.
  assets_folder = os.path.join('', 'static/js')
  return send_from_directory(assets_folder, filename)



@app.route('/classifieds/postad', methods=['GET','POST'])
def postad():

    if  request.method =='GET':

        if 'Authenticated' in request.cookies:

            if request.cookies.get('Authenticated') =='Yes':

                resp =make_response(render_template('postad.html',session_variable=str(session['username'])))

            else:
                resp =make_response(render_template('404_error.html',session_variable=str(session['username'])))
        else:
                resp =render_template('404_error.html')


    if  request.method =='POST':

        if 'Authenticated' in request.cookies:

            if request.cookies.get('Authenticated') =='Yes':

                filepath=[]

                # save each "charts" file

                for file in request.files.getlist('pics'):
                    if file.filename!='':
                        uploadedFile=secure_filename(file.filename)
                        filepathstring=os.path.join("uploads", uploadedFile)

                        file.save(filepathstring)
                        filepath.append(filepathstring)

                #session['adPosted']='Yes'


                print(request)
                createAd(session['username'],request,filepath)
                #user = User(index=row[0], country=row[1],age = row[2],gender=row[3], fear = row[4], anxious = row[6], anger = row[6], happiness = row[7], sadness = row[8], emotionalBigImpact = row[9], reason = row[10], mostMeaning = row[11], occupation = row[12], addField1 = row[13], addField2 = row[14], addField3 = row[15])
                #db.session.add(user)
                #db.session.commit()



                recentAdslist=getRecentAds()
                myAdsList=getMyAds(session['username'])
                #resp =make_response(render_template('home.html',session_variable1=str(session['username']),recentAdslist=recentAdslist,myAdsList=myAdsList))
                #resp.set_cookie('adPosted', 'Yes')

                confirmMessage1='Hurrah, your Ad is posted successfully!!!'
                confirmMessage2='Please verify if your Ad is displayed correctly in MyAds page'
                redirection='/classifieds'
                return render_template('confirmation.html',confirmMessage1=confirmMessage1,confirmMessage2=confirmMessage2,redirection=redirection)
                #resp= redirect(url_for('home'))



                #return resp
            else:
                resp =make_response(render_template('404_error.html',session_variable=str(session['username'])))
                return resp
        else:
                resp =render_template('404_error.html')
                return resp







    #return resp
    #return render_template('index.html',group1=group1_list,country_list1=country_list1,group2=group2_list,country_list2=country_list2)



@app.route('/search_classifieds', methods=['POST'])
def adSearch():

    if 'username' not in session:
        session['username']='Guest'
        recentAdslist=getRecentAds()
        searchads = getSearchAds(request)
        resp =make_response(render_template('index.html',session_variable=str(session['username']),searchAdsList=searchads,recentAdsList=recentAdslist))
        resp.set_cookie('Authenticated', 'No')

    elif session['username']=='Guest':
        recentAdslist=getRecentAds()
        searchads = getSearchAds(request)
        resp =make_response(render_template('index.html',session_variable=str(session['username']),searchAdsList=searchads,recentAdsList=recentAdslist))
        resp.set_cookie('Authenticated', 'No')

    else:
        recentAdslist=getRecentAds()
        searchads = getSearchAds(request)
        myAdsList=getMyAds(session['username'])
        profileInfo=getUserDetails(session['username'])
        resp =make_response(render_template('home.html',session_variable=str(session['username']),searchAdsList=searchads,recentAdsList=recentAdslist,myAdsList=myAdsList,profileInfo=profileInfo))
        resp.set_cookie('Authenticated', 'Yes')

    return resp
    #return render_template('index.html',group1=group1_list,country_list1=country_list1,group2=group2_list,country_list2=country_list2)




    return render_template('index.html',group1=group1_list,country_list1=country_list1,group2=group2_list,country_list2=country_list2,group3=group3_list,country_list3=country_list3,group4=group4_list,country_list4=country_list4)
    #return render_template('index.html',group1=group1_list,country_list1=country_list1,group2=group2_list,country_list2=country_list2)









def getAdDetails(adId):

    records=AdDetails.query.with_entities(AdDetails.adTitle,AdDetails.adDescription,AdDetails.adType,AdDetails.expectedPrice,AdDetails.payFrequency,AdDetails.postedDate,AdDetails.adId).filter(AdDetails.adId==adId).all()
    userId=AdsList.query.with_entities(AdsList.userId).filter(AdsList.adId==adId).all()
    userRecord=UserDetails.query.with_entities(UserDetails.fname,UserDetails.lname).filter(UserDetails.userId==userId[0][0]).all()
    email=Register.query.with_entities(Register.emailId).filter(Register.userId==userId[0][0]).all()
    adFiles=AdFiles.query.with_entities(AdFiles.adFilePath).filter(AdFiles.adId==adId).all()
    list1=[]
    list3=[]
    List5=[]

    for record in records:
        list2=[]
        list2.append(record.adTitle)
        list2.append(record.adDescription)
        list2.append(record.adType)
        list2.append(record.expectedPrice)
        list2.append(record.postedDate)
        list2.append(record.payFrequency)
        list2.append(record.adId)
        list1.append(list2)


    for record in userRecord:
        list4=[]
        list4.append(record.fname)
        list4.append(record.lname)
        list4.append(email)
        list3.append(list4)



    for record in adFiles:
        list4=[]
        list4.append(record.adFilePath.replace('\\','/'))

        List5.append(list4)

    return list1,list3,List5



def getUserDetails(username):

    #records=AdDetails.query.with_entities(AdDetails.adTitle,AdDetails.adDescription,AdDetails.adType,AdDetails.expectedPrice,AdDetails.payFrequency,AdDetails.postedDate,AdDetails.adId).filter(AdDetails.adId==adId).all()
    #userId=AdsList.query.with_entities(AdsList.userId).filter(AdsList.adId==adId).all()
    userId=Register.query.with_entities(Register.userId).filter(Register.emailId==username).all()
    password=Register.query.with_entities(Register.password).filter(Register.emailId==username).all()
    userRecord=UserDetails.query.with_entities(UserDetails.fname,UserDetails.lname,UserDetails.dob,UserDetails.address,UserDetails.city,UserDetails.state,UserDetails.country,UserDetails.zip,UserDetails.phone).filter(UserDetails.userId==userId[0][0]).all()

    list1=[]
    list2=[]



    for record in userRecord:
        list1=[]
        list1.append(username)
        list1.append(record.fname)
        list1.append(record.lname)
        list1.append(record.dob)
        list1.append(record.address)
        list1.append(record.city)
        list1.append(record.state)
        list1.append(record.country)
        list1.append(record.zip)
        list1.append(record.phone)
        list1.append(password[0][0])
        list2.append(list1)


    return list2



def createAd(username,request,filepath):

    postedDate=datetime.strptime(request.form.get('datepicker'), '%m%d%Y')
    adDetails = AdDetails(adTitle=request.form.get('Title'), adDescription=request.form.get('Description'),adType = request.form.get('Ad_Type'),expectedPrice = request.form.get('Price'), payFrequency = request.form.get('Frequency'), postedDate =postedDate , status = 'Open')
    db1.session.add(adDetails)
    db1.session.commit()

    userId=email=Register.query.with_entities(Register.userId).filter(Register.emailId==username).all()
    for file in filepath:
        adFiles=AdFiles(adFilePath=file,adId=adDetails.adId)
        db1.session.add(adFiles)
        db1.session.commit()

    adList=AdsList(adId=adDetails.adId,userId=userId[0][0])
    db1.session.add(adList)
    db1.session.commit()




def createUser(request):

    postedDate=datetime.strptime(request.form.get('datepicker'), '%m%d%Y')
    register = Register(emailId=request.form.get('Email'), password=request.form.get('Password'),role = 'Member', status = 'active')
    db1.session.add(register)
    db1.session.commit()



    userdetails=UserDetails(userId=register.userId,fname=request.form.get('Fname'),lname=request.form.get('Lname'),dob=postedDate,address=request.form.get('Address'),city=request.form.get('City'),state=request.form.get('State'),country=request.form.get('Country'),zip=request.form.get('Zip'),phone=request.form.get('Phone'))
    db1.session.add(userdetails)
    db1.session.commit()



def updateUser(request):

    postedDate=datetime.strptime(request.form.get('datepicker'), '%Y-%m-%d')
    userRecords=Register.query.filter(Register.emailId==request.form.get('Email')).all()

    for userRecord in userRecords:
        userRecord.emailId=request.form.get('Email')
        userRecord.password=request.form.get('Password')
        db1.session.commit()


    userdetails=UserDetails.query.filter(UserDetails.userId==userRecord.userId).all()

    for userdetail in userdetails:

        userdetail.fname=request.form.get('Fname')
        userdetail.lname=request.form.get('Lname')
        userdetail.dob=postedDate
        userdetail.address=request.form.get('Address')
        userdetail.city=request.form.get('City')
        userdetail.state=request.form.get('State')
        userdetail.country=request.form.get('Country')
        userdetail.zip=request.form.get('Zip')
        userdetail.phone=request.form.get('Phone')
        db1.session.commit()






def getSearchAds(request):
    records=AdDetails.query.with_entities(AdDetails.adTitle,AdDetails.adType,AdDetails.expectedPrice,AdDetails.postedDate,AdDetails.payFrequency,AdDetails.adId).filter(AdDetails.adType.like(request.form.get('Ad_Type'))).filter((AdDetails.adTitle.like("%" + request.form.get('Search_for_Keyword') + "%")) | (AdDetails.adDescription.like("%" + request.form.get('Search_for_Keyword') + "%"))).all()
    print(records)
    print(request.form.get('Ad_Type'))
    #records=surveyUser.query.filter(temp1).filter(temp2).all()
    list1=[]

    for record in records:
        list2=[]
        list2.append(record.adTitle)
        list2.append(record.adType)
        list2.append(record.expectedPrice)
        list2.append(record.postedDate)
        list2.append(record.payFrequency)
        list2.append(record.adId)
        list1.append(list2)

    return list1



def getRecentAds():

    records=AdDetails.query.with_entities(AdDetails.adTitle,AdDetails.adType,AdDetails.expectedPrice,AdDetails.postedDate,AdDetails.payFrequency,AdDetails.adId).order_by(AdDetails.postedDate).limit(15).all()
    #records=surveyUser.query.filter(temp1).filter(temp2).all()
    list1=[]

    for record in records:
        list2=[]
        list2.append(record.adTitle)
        list2.append(record.adType)
        list2.append(record.expectedPrice)
        list2.append(record.postedDate)
        list2.append(record.payFrequency)
        list2.append(record.adId)
        list1.append(list2)

    return list1




def getMyAds(username):


    currentuserId=Register.query.with_entities(Register.userId).filter(Register.emailId==username).all()
    adIdList=AdsList.query.with_entities(AdsList.adId).filter(AdsList.userId==currentuserId[0][0]).subquery()


    records=AdDetails.query.join(adIdList,AdDetails.adId==adIdList.c.adId).with_entities(AdDetails.adTitle,AdDetails.adType,AdDetails.expectedPrice,AdDetails.postedDate,AdDetails.payFrequency,AdDetails.adId).order_by(AdDetails.postedDate).all()
    #records=surveyUser.query.filter(temp1).filter(temp2).all()
    list1=[]

    for record in records:
        list2=[]
        list2.append(record.adTitle)
        list2.append(record.adType)
        list2.append(record.expectedPrice)
        list2.append(record.postedDate)
        list2.append(record.payFrequency)
        list2.append(record.adId)
        list1.append(list2)

    return list1




def CheckLogin(email,password):
    records=Register.query.with_entities(Register.userId,Register.emailId).filter(Register.emailId==email).filter(Register.password==password).filter(Register.status=='active').all()
    #records=surveyUser.query.filter(temp1).filter(temp2).all()
    list1=[]
    #group3_records=User.query.filter(User.age<=35).filter(User.gender=='Female').group_by(User.country).all()
    #group4_records=User.query.filter(User.age>=36).filter(User.gender=='Female').group_by(User.country).all()
    for record in records:
        list2={}
        list2['userId']=record.userId
        list2['emailId']=record.emailId
        list1.append(list2)

    return list1





if __name__ == '__main__':
    # get current app directory

    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
    app.run(debug = True, port=5287)
