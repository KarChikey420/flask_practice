from flask import Flask,request,jsonify
from flask_Jwt_Extended import (JWTManager,create_access_token
                                ,jwt_required,get_jwt_identity)
from datetime import timedelta
from werkzeug.security import generate_password_hash,check_password_hash

app=Flask(__name__)

app.config["JWT_SECRET_KEY"]="mysecretkey"
app.config["JWT_ACCESS_TOKEN_EXPIRES"]=timedelta(minutes=30)

jwt=JWTManager(app)

USERS = {
    "kartikey": generate_password_hash("kartikey@123")
}

@app.route("/login",methods=["POST"])
def login():
   data=request.get_json()
   username=data.get("username")
   password=data.get("password")
   
   if username not in USERS