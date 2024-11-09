from flask import Flask, request, jsonify
from flask_cors import CORS
from responseTextFromLama import process_query
#when calling from the react app we need to enable the cors policy as in this 
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define a separate function to process the input
def process_input(input_value):
    # Example Python code execution
    result = f"Processed input: {input_value}"
    return result

@app.route('/run-code', methods=['POST'])
async def run_code():
    data = request.json
    input_value = data.get('query', None)
    response_text = await process_query(input_value)
    if response_text is None:
        return jsonify({"error": "No input provided"}), 400

    # Call the function to process the input
    result = response_text
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
