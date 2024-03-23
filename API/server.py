from flask import Flask, jsonify

app = Flask(__name__)

# Define a route for the root endpoint
@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the API!'})

# Define a route for a sample endpoint
@app.route('/api/sample')
def sample():
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
