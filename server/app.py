from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!, happy 2020"

@app.route('/todos', methods=['GET'])
def getTodos():
    todos = [
        {
            'title': 'Sleep',
            'status': False
        },
        {
            'title': 'Movie',
            'status': False
        }
    ]
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def addTodo():
    return 'adad'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000, debug=True)