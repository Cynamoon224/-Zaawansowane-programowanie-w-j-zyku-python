from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/test')  
def hello_world():
    return jsonify({'hello': 'world2'})

if __name__ == '__main__':
    app.run(debug=True)
