from flask_sqlalchemy import SQLAlchemy
from __main__ import app


#db = SQLAlchemy(app)
db2 = SQLAlchemy(app)

class Register(db2.Model):
    __tablename__ = 'Register'
    userId = db2.Column(db2.Integer, primary_key=True, nullable=False)    
    emailId = db2.Column(db2.String(50), unique = True, nullable=False)    
    password = db2.Column(db2.String(16), nullable=False)  
    active = db2.Column(db2.String(5), nullable=False)
    