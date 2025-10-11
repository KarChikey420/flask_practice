from flask import Flask,jsonify,request
from flask import SQLALchemy

app=Flask(__name__)

app.config["sqlalchemy_database_uri"]=""
app.config["sqlalchemy_track_modification"]=False

db=SQLALchemy(app)

class User(db.model):
    __table__='Employee'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    role=db.Column(db.String(100),nullable=False)
    
    def to_dict(self):
        return {"id":self.id,"name":self.name,"role":self.role}
    
@app.route("/")
def Home():
    return "Flask + Backend Running"

@app.route("/users",method=['GET'])
def get_users():
    users=User.query