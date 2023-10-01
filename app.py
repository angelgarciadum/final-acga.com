from flask import Flask, render_template
from mongo import MongoConnection
import atexit

app = Flask(__name__)

db_client = MongoConnection().client
db = db_client.get_database('drones')
col = db.get_collection('products')

@app.route('/')
def index():
    products_data = col.find({})
    return render_template('index.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True)