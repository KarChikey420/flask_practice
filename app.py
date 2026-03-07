from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:root@localhost:5432/mydb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)

class User(db.Model):
    __tablename__='Employee'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    role=db.Column(db.String(100),nullable=False)
    
    def to_dict(self):
        return {"id":self.id,"name":self.name,"role":self.role}
    
@app.route("/")
def Home():
    return "Flask + Backend Running"

@app.route("/users",methods=['GET'])
def get_users():
    users=User.query.all()
    return jsonify([u.to_dict() for u in users])

@app.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    user=User.query.get(user_id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({"error":"user not found"}),404

@app.route('/user/',methods=['POST'])
def add_user():
    data=request.get_json()
    new_user=User(name=data['name'],role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"user added successfully"}),201

@app.route('/user/<int:user_id>',methods=['PUT'])
def update_user(user_id):
    user=User.query.get(user_id)
    if not user:
        return jsonify({"error":"user not found"}),404
    
    data=request.get_json()
    user.name=data.get('name',user.name)
    user.role=data.get('role', user.role)
    db.session.commit()
    return jsonify({"message":"user updated successfully"})

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user=User.query.get(user_id)
    if not user:
        return jsonify({"error":"user not found"}),404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message":"user deleted successfully"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
