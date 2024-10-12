"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Personajes, Planetas, Usuario, Datos_Favoritos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
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

@app.route('/personajes', methods=['GET'])
def Get_Personajes():
    all_Personajes= Personajes.query.all()
    print(all_Personajes)
    results = list(map(lambda Gender : Gender.serialize(), all_Personajes))
    return jsonify(results), 200

@app.route('/personajes/<int:personajes_id>', methods=['GET'])
def Get_Personajes_id(personajes_id):
    print(personajes_id)
    identification= Personajes.query.filter_by(Id_Personajes = personajes_id).first()
    return jsonify(identification.serialize()), 200

@app.route('/personajes', methods=['POST'])
def POST_Personajes():
    body = request.get_json()
    box = Personajes(Birthline = body['Birthline'], Gender = body['Gender'], Height = body['Height'], Skin_color = body['Skin_color'], Eye_color = body['Eye_color'])
    db.session.add(box)
    db.session.commit()
    response_body = {
        "msg": "A person has been added"
    }
    return jsonify(response_body), 200

@app.route('/planetas', methods=['GET'])
def Get_Planetas():
    all_Planetas = Planetas.query.all()
    print(all_Planetas)
    results = list(map(lambda Rotation_Period : Rotation_Period.serialize() ,all_Planetas))
    return jsonify(results), 200

@app.route('/planetas/<int:planetas_id>', methods=['GET'])
def Get_Planetas_id(planetas_id):
    print(planetas_id)
    identification= Planetas.query.filter_by(ID_Planeta = planetas_id).first()
    return jsonify(identification.serialize()), 200

@app.route('/usuario', methods=['GET'])
def Get_usuario():
    all_usuario = Usuario.query.all()
    print(all_usuario)
    results_usuario = list(map(lambda Nombre : Nombre.serialize() ,all_usuario))
    return jsonify(results_usuario), 200

@app.route('/favorite/planet', methods=['POST'])
def add_favorite_planet():
    body = request.get_json()
    new_favorite = Datos_Favoritos(user_Id=body['user_Id'], Planeta_ID=body['Planeta_ID'])
    db.session.add(new_favorite)
    db.session.commit()
    response_body = {
        "msg": "A favorite planet has been added to the user"
    }
    return jsonify(response_body), 200

@app.route('/favorite/personajes', methods=['POST'])
def add_favorite_personajes():
    body = request.get_json()
    new_favorite = Datos_Favoritos(user_Id=body['user_Id'], Personajes=body['Personajes'])
    db.session.add(new_favorite)
    db.session.commit()
    response_body = {
        "msg": "A favorite person has been added to the user"
    }
    return jsonify(response_body), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)





 