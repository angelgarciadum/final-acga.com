from flask import Flask
from flask import render_template
from dotenv import load_dotenv
from mongo import MongoConnection

load_dotenv()

app = Flask(__name__)

db_client = MongoConnection().client
db = db_client.get_database('tiendamia')
col = db.get_collection('drones')
@app.route('/')
def index():
    products_data = col.find({})
    return render_template('index.html', drones=products_data)

if __name__ == '__main__':
    app.run(debug=True)