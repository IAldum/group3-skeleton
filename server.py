from flask import Flask, request, jsonify
import requests
import findapet

state = 'NO_QUERY'
context = {}


app = Flask(__name__)

# A basic homepage, to check everything is working.
@app.route('/',  methods=['POST', 'GET'])
def index():
    global state
    global context
    
    line = request.values.get('text') or ''
 
    ret = findapet.ON_INPUT[state](line, context) 

    state, context, optional_output = ret
    if optional_output:
        #
        return jsonify({
        'reponse_type': 'in_channel',
        'text': optional_output
    })
    
    else:
        output = findapet.ON_ENTER_STATE[state](context)
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