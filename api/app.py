
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient("mongodb+srv://own:123@datta.iaz7e.mongodb.net/?retryWrites=true&w=majority&appName=datta")
db = client.newsletter
subscribers = db.subscribers

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/newsletter', methods=['POST'])
def newsletter():
    data = request.get_json()
    email = data.get('email')
    if email:
        try:
            subscribers.insert_one({"email": email})
            return jsonify({"message": "Subscribed successfully!"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "Invalid email"}), 400

# Export the app for Vercel
app = app
