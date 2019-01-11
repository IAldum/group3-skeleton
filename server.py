from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# A basic homepage, to check everything is working.
@app.route('/')
def index():
    return "Welcome to Group 3's project!"

# A basic slack endpoint.
@app.route('/mycommand', methods=['POST'])
def mycommand_endpoint():
    message = request.form.get('text')
    return f"You said {message}"

if __name__ == '__main__':
    app.run(debug=True)