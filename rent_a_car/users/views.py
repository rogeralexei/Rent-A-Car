from werkzeug.security import check_password_hash, generate_password_hash
from rent_a_car import users_collection,cars_collection, app,session_handler
from flask import jsonify, request,url_for,redirect,session
from bson.json_util import ObjectId,loads

# Ruta de Registro
@app.route("/register", methods=["GET","POST"])
def register():
    if session_handler():
        return jsonify({"message": "Ya te encuentras loggeado como {}".format(session["username"])})
    if request.method=="POST":
        username=request.json["username"]
        password=request.json["password"]
        found_user=users_collection.find_one({"username":username})
        if not found_user:
            users_collection.insert_one({"username":username,"password": generate_password_hash(password), "carro": False})
            return jsonify({"message": "Usuario Añadido con exito"})
        else:
            return jsonify({"message": "El usuario que intentas registrar no esta disponible. Intenta denuevo"})
    return jsonify({"message": "Necesitas enviar un Post Request a register para registrarte"})

#Ruta de Login
@app.route("/login", methods=["GET","POST"])
def login():
    if session_handler():
        return jsonify({"message": "Ya te encuentras loggeado como {}".format(session["username"])})
    if request.method=="POST":
        username=request.json["username"]
        password=request.json["password"]
        found_user=users_collection.find_one({"username":username})
        if found_user!=None and check_password_hash(found_user["password"],password):
            session["username"]=username
            session.permantent=True
            return jsonify({"message":"Logeado correctamente como {}".format(session["username"])})
        return jsonify({"message":"El usuario no ha sido creado o el password es incorrecto. Verificar Credenciales"})
    return jsonify({"message":"Necesitas Iniciar sesion primero mediante a un POST Request"})

#Ruta profile
@app.route("/user/<username>")
def profile(username):
    if session_handler()==username:
        obj=users_collection.find_one({"username":username})
        output=[]
        output.append({"_id":str(obj["_id"]),"username": obj["username"], "password": obj["password"], "carro":str(loads(obj["carro"]))})
        return jsonify({"message": "Bienvenido a tu perfil {}".format(session["username"])},{"resultado": output})
    return jsonify({"message": "Este no es tu perfil o no te has loggeado. Verifica tu informacion."})

#Listar Usuarios
@app.route("/user/list_users")
def users():
    if session_handler():
        objects=users_collection.find()
        ouput=[]
        for obj in objects:
            if obj["carro"]:
                deserialized_id=loads(obj["carro"])
                carro=cars_collection.find_one({"_id": ObjectId(deserialized_id)}) 
                d_carro={"_id": str(carro["_id"]), "modelo":carro["modelo"],"marca": carro["marca"],"año": carro["año"], "kilometraje": carro["kilometraje"]}
                ouput.append({"username":obj["username"], "password":obj["password"], "carro": d_carro})
            else:
              ouput.append({"username":obj["username"], "password":obj["password"], "carro": obj["carro"]})
        return jsonify({"result": ouput})
    return jsonify({"message": "Necesitas Loggearte para ver la lista de usuarios primero"})

#Ruta de Logout
@app.route("/logout")
def logout():
    session.pop("username",None)
    return jsonify({"message":"Logout exitoso"})

