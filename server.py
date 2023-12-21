from flask import Flask, request

#port
port = 8080

# Create a Flask server instance
app = Flask(__name__)

#Home Page
@app.route('/')
def home():
  return {'Done' : 'Success'}