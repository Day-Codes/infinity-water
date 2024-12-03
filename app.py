from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
from termcolor import colored  # For colored console output
import os

app = Flask(__name__)

# MongoDB Configuration (replace with your actual connection string)
client = MongoClient("mongodb+srv://own:123@datta.iaz7e.mongodb.net/?retryWrites=true&w=majority&appName=datta")
db = client.newsletter
subscribers = db.subscribers

# Maintenance Mode Flag
maintenance_mode = False  # Set this to True to enable maintenance mode

# Fancy Startup Message with Console Color
def fancy_startup_message():
    startup_message = """
    ========================================================
    Welcome to Infinite Water™ Backend!
    Powered by Flask, MongoDB, and Python!
    ========================================================
    """
    print(colored(startup_message, 'cyan'))
    print(colored("Running on Flask | MongoDB Integration", 'yellow'))
    print(colored("Server is starting on port 5000", 'green'))
    print(colored("Press CTRL+C to shut down the server", 'red'))
    print("========================================================")

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Newsletter Subscription Route
@app.route('/newsletter', methods=['POST'])
def newsletter():
    email = request.form.get('email')  # Get the email from the form submission
    
    if email:
        # Add the email to your database or perform any other necessary action
        # For now, let's just send a success message
        return jsonify({'message': 'Successfully subscribed to the newsletter!'})
    else:
        return jsonify({'message': 'Please provide a valid email address.'}), 400

# Analytics Route (Password Protected)
@app.route('/analytics', methods=['GET'])
def analytics():
    password = request.args.get('password')
    if password != 'your_admin_password':  # Replace with a strong password
        return redirect(url_for('home'))

    subscriber_count = subscribers.count_documents({})
    return render_template('analytics.html', subscriber_count=subscriber_count)

# Error Handling Routes
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Maintenance Mode Check
@app.before_request
def check_maintenance():
    if maintenance_mode:
        return render_template('maintenance.html')

if __name__ == '__main__':
    fancy_startup_message()
    app.run(debug=True, host='0.0.0.0', port=5000)
