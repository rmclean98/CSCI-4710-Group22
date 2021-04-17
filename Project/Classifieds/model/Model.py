from flask_sqlalchemy import SQLAlchemy
from __main__ import app


#db = SQLAlchemy(app)
db1 = SQLAlchemy(app)



class UserDetails(db1.Model):
    __tablename__ = 'UserDetails'
    userDetailsId = db1.Column(db1.Integer, primary_key=True)
    userId = db1.Column(db1.Integer, db1.ForeignKey('Register.userId'))      
    fname = db1.Column(db1.String(50), nullable=False)     
    lname = db1.Column(db1.String(50), nullable=False)   
    dob = db1.Column(db1.DateTime, nullable=False)
    address = db1.Column(db1.String(500)) 
    city = db1.Column(db1.String(50)) 
    state = db1.Column(db1.String(50)) 
    country = db1.Column(db1.String(50)) 
    zip = db1.Column(db1.Integer)
    phone = db1.Column(db1.String(15))



class Register(db1.Model):
    __tablename__ = 'Register'
    userId = db1.Column(db1.Integer, primary_key=True, nullable=False)    
    emailId = db1.Column(db1.String(50), unique = True, nullable=False)    
    password = db1.Column(db1.String(16), nullable=False)
    role =  db1.Column(db1.String(20), nullable=False) 
    status = db1.Column(db1.String(5), nullable=False)


class AdDetails(db1.Model):
    __tablename__ = 'AdDetails'
    adId = db1.Column(db1.Integer, primary_key=True,nullable=False)
    adTitle = db1.Column(db1.String(300), nullable=False)      
    adDescription = db1.Column(db1.String(3500), nullable=False)     
    adType = db1.Column(db1.String(50), nullable=False)   
    expectedPrice = db1.Column(db1.Numeric(10,2), nullable=False)
    payFrequency = db1.Column(db1.String(100)) 
    postedDate = db1.Column(db1.DateTime, nullable=False) 
    status = db1.Column(db1.String(50)) 



class AdsList(db1.Model):
    __tablename__ = 'AdsList'
    adsListId = db1.Column(db1.Integer, primary_key=True, nullable=False) 
    adId = db1.Column(db1.Integer, db1.ForeignKey('AdDetails.adId'))
    userId = db1.Column(db1.Integer, db1.ForeignKey('Register.userId'))


class AdFiles(db1.Model):
    __tablename__ = 'AdFiles'
    adFileId = db1.Column(db1.Integer, primary_key=True, nullable=False) 
    adId = db1.Column(db1.Integer, db1.ForeignKey('AdDetails.adId'))
    adFilePath = db1.Column(db1.String(200), nullable=True)
    

    


    



    