from flask import Flask, request, jsonify

app = Flask(__name__)

# Root route to guide users
@app.route('/')
def home():
    return '''
    <h2>Welcome to the Even Numbers API</h2>
    <p>To get the first N even numbers, use:</p>
    <code>/even-numbers?n=5</code>
    <p>Example: <a href="/even-numbers?n=10">/even-numbers?n=10</a></p>
    '''

# Route to return N even numbers
@app.route('/even-numbers', methods=['GET'])
def even_numbers():
    try:
        n = int(request.args.get('n', 10))
        even_list = [i for i in range(2, 2 * n + 1, 2)]
        return jsonify(even_list)
    except ValueError:
        return jsonify({'error': 'Invalid value for n. Please provide an integer.'}), 400

if __name__ == '__main__':
    app.run()