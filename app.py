from flask import request, jsonify, render_template
from conn import app, db, lunch_schema, lunchs_schema
from models import Lunch
from sqlalchemy import desc
import re

#Index
@app.route('/')
def index():
 return render_template('index.html')

#Create Lunch
@app.route('/lunchs', methods=['POST'])
def addLunch():
    try:
        name = request.json['name']
        lastname = request.json['lastname']
        telephone = request.json['telephone']
        email = request.json['email']
        age = request.json['age']
        address = request.json['address']
        food_delivered = request.json['food_delivered']
        observation = request.json['observation']
    
        new_lunch = Lunch(name, lastname, telephone, email, age, address, food_delivered, observation)
    
        db.session.add(new_lunch)
        db.session.commit()
    
        return lunch_schema.jsonify(new_lunch)
    except Exception:
        return jsonify({'Message': "No data found - Contact With Support"})

#get all Lunchs
@app.route('/lunchs', methods=['GET'])
def getLunchs():
    all_lunchs = Lunch.query.all()
    result = lunchs_schema.dump(all_lunchs)
        
    return jsonify(Lunchs=result)

#Get all Lunchs per page
@app.route('/lunchs/page=<int:page>', methods=['GET'])
def getLunchsPerPage(page):
    try:
        all_lunchs = Lunch.query.order_by(desc(Lunch.id)).paginate(page=page, per_page=10).items
        result = lunchs_schema.dump(all_lunchs)
        
        return jsonify(Lunchs=result)
    
    except Exception:
        return jsonify({'Message': "No data found - Contact With Support"})

#Lunch order by asc/desc
@app.route('/lunchs/order=<param>', methods=['GET'])
def getLunchsAD(param):
    try:
        if param == 'asc':
            all_lunchs = Lunch.query.order_by(Lunch.name).all()
            result = lunchs_schema.dump(all_lunchs)
            
            return jsonify(Lunchs=result)
        elif param == 'desc':
            all_lunchs = Lunch.query.order_by(desc(Lunch.name)).all()
            result = lunchs_schema.dump(all_lunchs)
            
            return jsonify(Lunchs=result)
        elif param == 'age':
            all_lunchs = Lunch.query.order_by(desc(Lunch.age)).all()
            result = lunchs_schema.dump(all_lunchs)
            
            return jsonify(Lunchs=result)
    
    except Exception:
        return jsonify({'Message': "No data found - Contact With Support"})

#Search by ID, Name, Email
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      return True
    else:
      return False

@app.route('/lunchs/<param>', methods=['GET'])
def getLunch(param):
    try:
        if param.isnumeric():
            lunch = Lunch.query.get_or_404(param)
            return lunch_schema.jsonify(lunch)
        elif type(param) == str:
            if isValid(param):
                lunch = Lunch.query.filter_by(email=param).first()
                return lunch_schema.jsonify(lunch)
            else:
                lunch = Lunch.query.filter_by(name=param)
                return lunchs_schema.jsonify(lunch)
            
    except Exception:
        return jsonify({'Message': "No data found - Contact With Support"})

#Update Lunch
@app.route('/lunchs/<id>', methods=['PUT'])
def updateLunch(id):
    try:
        lunch = Lunch.query.get_or_404(id)

        name = request.json['name']
        lastname = request.json['lastname']
        telephone = request.json['telephone']
        email = request.json['email']
        age = request.json['age']
        address = request.json['address']
        food_delivered = request.json['food_delivered']
        observation = request.json['observation']
        
        lunch.name = name
        lunch.lastname = lastname
        lunch.telephone = telephone
        lunch.email = email
        lunch.age = age
        lunch.address = address
        lunch.food_delivered = food_delivered
        lunch.observation = observation
        
        db.session.commit()
        
        return lunch_schema.jsonify(lunch)
    
    except Exception:
        return jsonify({'Message': "No data found - Contact With Support"})
    
#Delete Lunch
@app.route('/lunchs/<id>', methods=['DELETE'])
def deleteLunch(id):
    try:
        lunch = Lunch.query.get_or_404(id)
        db.session.delete(lunch)
        db.session.commit()

        return lunch_schema.jsonify(lunch)
    
    except Exception:
        return jsonify({'Message': "No data found - Contact With Support"})
    
#Start run server
if __name__ == "__main__":
    app.run(debug=True)