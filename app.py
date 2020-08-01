from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MONGO_DBNAME'] = 'accidents_mx'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/accidents_mx'

mongo = PyMongo(app)

@app.route("/entidad/<entidad>", methods=['GET'])
def index(entidad):
    collection = mongo.db.accidents
    output = []
    for acc in collection.find({'ID_ENTIDAD': int(entidad)}):
        acc['_id'] = str(acc['_id'])
        output.append(acc)
    return jsonify({'data' : output})
    
if __name__ == "__main__":
    app.run(debug=True)
