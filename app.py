from rent_a_car import db,app
from rent_a_car.cars import views
from rent_a_car.users import views
from flask import jsonify, session
import datetime

app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(minutes=30)

@app.route("/")
def index():
    return jsonify({"message": "Bienvenido a la api para rentar carros. Te recomiendo vayas al endpoint '/register' para registrarte primero"})

@app.errorhandler(404)
def not_found(e):
    return jsonify({"message": "404, pagina no encontrada."})
    
if __name__ == "__main__":
    app.run()