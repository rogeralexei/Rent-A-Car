import pymongo
from flask import Flask, jsonify, request,session

app=Flask(__name__)

client=pymongo.MongoClient("localhost",27017)
db=client.rent_a_car
cars_collection=db.cars
users_collection=db.users

#Por temas de seguridad se deberia usar un env variable. Pero como es una app de testing y es en entorno local
#no hay que preocuparse por eso
app.config["SECRET_KEY"]="mytestkey" 

def session_handler():
    try:
        current_user=session["username"]
    except KeyError:
        current_user=None
    return current_user
                                    