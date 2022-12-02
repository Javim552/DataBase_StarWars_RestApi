"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, json
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db




app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints

@app.route('/')
def sitemap():
    return generate_sitemap(app)

# TRABAJAR CON PEOPLE
@app.route('/character', methods=['GET'])
def mostrarCharacter():
    charactersAll = Character.query.all ()
    resultado = []
    resultado = [character.serialize () for character in charactersAll]
    return jsonify(resultado),200
    

@app.route('/characters/<int:id>', methods=['GET'])
def mostrarOneCharacter(id):
    onecharacter = Character.query.filter_by(id=id).one()
    onecharacter = onecharacter.serialize()
    return jsonify(onecharacter),200

@app.route('/characters', methods=['POST'])
def createCharacter():
    data = request.data
    data = json.loads (data)
    character = character(name = data.name)
    db.session.add(character)
    db.session.commit()


@app.route('/character/<int:id>', methods=['DELETE'])
def deleteCharacter():
    character = Characer.query.get(1)
    db.session.delete(character)
    db.session.commit()

#TRABAJAR CON PLANETS

@app.route('/planets', methods=['GET'])
def mostrarPlanets ():
    planetsAll = Planets.query.all()
    resultado= []
    resultado = [planets.serialize () for planets in planetsAll]
    return jsonify(planets),200

@app.route('/planets/<int:planets_id>', methods=['GET'])
def mostrarOnePlanet (planets_id):
    oneplanet = Planets.query.filter_by(id=id).one()
    oneplanet=oneplanet.serialize()
    return jsonify(oneplanet), 200

@app.route('/planets', methods=['POST'])
def createPlanet():
    data = request.data
    data = json.loads (data)
    planets = planets(name = data.name)
    db.session.add(planets)
    db.session.commit()

@app.route('/planets/<int:id>', methods=['DELETE'])
def deletePlanet():
    planets = planets.query.get(1)
    db.session.delete(planets)
    db.session.commit()
    

#MOSTRAR FAVORITOS


@app.route('/favoritos', methods=['GET'])
def mostrarfavoritos ():
    return jsonify(favoritos),200

@app.route('/favoritos/<int:favoritos_id>', methods=['GET'])
def mostrarOneFavorito (favoritos_id):
    oneFavorito = list(filter(lambda element: element["id"] == favoritos_id, favoritos))
    oneFavorito = oneFavorito [0]
    return jsonify(oneFavorito), 200










   

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
