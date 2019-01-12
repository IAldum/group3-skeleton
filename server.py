from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# A basic homepage, to check everything is working.
@app.route('/',  methods=['POST', 'GET'])
def index():
    message = request.form.get('text')
    return f"You said {message}"


# A basic slack endpoint.
@app.route('/mycommand', methods=['POST'])
def mycommand_endpoint():
    message = request.form.get('text')
    return f"You said {message}"

if __name__ == '__main__':
    app.run(debug=True)