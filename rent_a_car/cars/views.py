from rent_a_car import cars_collection ,users_collection, app,session_handler
from flask import jsonify, request,session
from bson.json_util import ObjectId,dumps

# Crear Nuevo Carro
@app.route("/nuevo_carro",methods=["POST"])
def api_post():
    if not session_handler():
        return jsonify({"message": "Necesitas Loggearte para añadir un nuevo carro"})
    output=[]
    new_car={ 
        "modelo": request.json["modelo"],
        "marca": request.json["marca"],
        "año": request.json["año"],
        "kilometraje": request.json["kilometraje"],
        "alquilado": False
    }
    cars_collection.insert_one(new_car)
    return jsonify({"message": "Carro Añadido exitosamente a la base de Datos"})

# Listar Carros
@app.route("/carros")
def api_get():
    objects=cars_collection.find()
    output=[]
    for obj in objects:
        if obj["alquilado"]:
            continue
        else:
            output.append({"_id":str(obj["_id"]),"modelo": obj["modelo"], "marca": obj["marca"],"año": obj["año"], "kilometraje": obj["kilometraje"]})
    if len(output)<1:
        return jsonify({"message": "No hay carros disponibles para alquilar"})
    return jsonify({"message": "Autos disponibles para alquilar","resultado": output})
    
#Ver carros de una marca especifica
@app.route("/carros/<marca>")
def api_show(marca):
    objects=cars_collection.find({"marca":marca})
    output=[]
    for obj in objects:
        if obj["alquilado"]:
            continue
        else:
            output.append({"_id":str(obj["_id"]),"modelo": obj["modelo"], "marca": obj["marca"],"año": obj["año"], "kilometraje": obj["kilometraje"], "alquilado":obj["alquilado"]})
    if len(output)>=1:
        return jsonify({"message": "Modelos de esa marca encontrados"},{"resultado": output})
    else:
        return jsonify({"message": "No tenemos autos de esa marca."})

#Editar un carro
@app.route("/editar_carro/<_id>", methods=["PUT"])
def api_put(_id):
    if not session_handler():
        return jsonify({"message": "Necesitas Loggearte para ver esta información"})
    nuevo_modelo=request.json["modelo"]
    nueva_marca=request.json["marca"]
    nuevo_ano=request.json["año"]
    nuevo_kilometraje=request.json["kilometraje"]
    output=[]
    try:
        serialized_id=ObjectId(_id)
    except:
        return jsonify({"message": "ID invalido"})
    obj=cars_collection.find_one_and_update({"_id": serialized_id}, {"$set":{"modelo":nuevo_modelo, "marca": nueva_marca, "año": nuevo_ano,"kilometraje": nuevo_kilometraje}})
    if obj:
        return jsonify({"message": "Carro actualizado exitosamente"})
    else:
        return jsonify({"message": "Not found"})

#Eliminar un carro
@app.route("/eliminar_carro/<_id>", methods=["DELETE"])
def api_delete(_id):
    if not session_handler():
        return jsonify({"message": "Necesitas Loggearte para ver esta información"})
    try:
        serialized_id=ObjectId(_id)
    except:
        return jsonify({"message":"ID Invalido"})
    obj=cars_collection.find_one_and_delete({"_id": serialized_id})
    print(obj)
    if obj!=None:
        return jsonify({"message": "Carro eliminado con exito de la base de datos"})
    else:
        return jsonify({"message": "Carro no encontrado"})

#Rentar un carro
@app.route("/rentar/<_id>", methods=["GET","POST"])
def rentar(_id):
    if not session_handler():
        return jsonify({"message": "Necesitas Loggearte para ver esta información"})
    if request.method=="POST":
        carro=cars_collection.find_one_and_update({"_id": ObjectId(_id)},{"$set":{"alquilado": True}})
        username=request.json["username"]
        user=users_collection.find_one_and_update({"username":username},{"$set":{"carro": dumps(carro["_id"])}})
        return jsonify({"message": "Carro rentado exitosamente"})
    return jsonify({"message": "Necesitas realizar un POST Request para alquilar un carro"})