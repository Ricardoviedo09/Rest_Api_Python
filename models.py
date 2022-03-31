from conn import db

#Lunch Class/Model
class Lunch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    lastname = db.Column(db.String(25), nullable=False)
    telephone = db.Column(db.Numeric, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(100))
    food_delivered = db.Column(db.Boolean, default=False, nullable=False)
    observation = db.Column(db.String(300))
    
    def __init__(self, name, lastname, telephone, email, age, address, food_delivered, observation):
        self.name = name
        self.lastname = lastname
        self.telephone = telephone
        self.email = email
        self.age = age
        self.address = address
        self.food_delivered = food_delivered
        self.observation = observation    

#Create Table if no exists        
db.create_all()