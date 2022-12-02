from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
        
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class UserDatos (db.Model):
    __tablename__ = "userDatos"
    id = db.Column (db.Integer, primary_key = True)
    userName = db.Column(db.String(250),nullable= False)
    lastUserName =db.Column(db.String(250),nullable = False)
    idfavoritos = db.Column(db.Integer, ForeignKey("favoritos.id"))
    favoritos = db.relationship("Favoritos")
    def __repr__(self):
       
        return '<UserDatos %r>' % self.username
     
    def serialize(self):
        return {
            "id": self.id,
            "userName": self.userName,
            "lasUserName":self.lastUserName,
            
            # do not serialize the password, its a security breach
        }


class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    namePerson = db.Column(db.String(250), nullable = False)

    def __repr__(self):
            
        return '<Characters %r>' % self.username
    
    def serialize(self):
        return {
            "id": self.id,
            "namePerson": self.namePerson,
                  
            # do not serialize the password, its a security breach
        }
                        
class Planets(db.Model):
    __tablename__ = 'planets'                   
    id = db.Column(db.Integer, primary_key=True)
    namePlanet = db.Column(db.String(250), nullable=False)

    def __repr__(self):
           
        return '<Planets %r>' % self.username
    
    def serialize(self):
        return {
            "id": self.id,
            "namePlanet": self.namePlanet,
                   
            # do not serialize the password, its a security breach
        }

class Favoritos(db.Model):
    __tablename__= "favoritos"
    id = db.Column(db.Integer, primary_key=True)
    idPlanet = db.Column(db.Integer, ForeignKey("planets.id"))
    idCharacter = db.Column(db.Integer, ForeignKey("characters.id"))
    
    def __repr__(self):
       
        return '<Favoritos %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
                  
            # do not serialize the password, its a security breach
        }



