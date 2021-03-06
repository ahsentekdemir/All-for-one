from flask import Flask, json, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from dataclass import dataclass
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db_service/main'

CORS(app)

db = SQLAlchemy(app)

@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass    
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

@app.route('/api/products')
def index():
    return jsonify(Product.query.all())

@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://0.0.0.1:8000/api/user')
    data = jsonify(req.json())
    try:
        productUser = ProductUser(user_id=data['id'], product_id=id)
        db.session.add(productUser)
        db.session.commit()
        
        # some event ll be there.  
    except:
        abort(400, 'u already like this product')
        
    return jsonify({
        'message': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
