from flask import Flask, request, jsonify
import requests
import findapet

state = 'NO_QUERY'
context = {}


app = Flask(__name__)
# for alexa
@app.route('/alexa', methods=['POST', 'GET'])
def alexa():
    return jsonify({
    'version': '0.1',
    'response': {
        'outputSpeech': {
        'type': 'PlainText',
        'text': 'Hello, welcome to my bot'
        }
        }
    })
    
# A basic homepage, to check everything is working.
@app.route('/',  methods=['POST', 'GET'])
def index():
    global state
    global context
    
    line = request.values.get('text') or ''
 
    ret = findapet.ON_INPUT[state](line, context) 

    state, context, optional_output = ret
    if optional_output:
        return jsonify({
        'reponse_type': 'in_channel',
        'text': optional_output
    })
    
    else:
        state, context, output = findapet.ON_ENTER_STATE[state](context)
        return jsonify({
        'reponse_type': 'in_channel',
        'text': output
    })
    

# A basic slack endpoint.
@app.route('/mycommand', methods=['POST'])
def mycommand_endpoint():
    message = request.form.get('text')
    return f"You said {message}"

if __name__ == '__main__':
    app.run(debug=True)