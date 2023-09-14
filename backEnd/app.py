from flask import Flask, jsonify

app = Flask(__name__)

# Define your version here
version = "1.2.0.0"

@app.route('/api/version')
def get_version():
    return jsonify({"version": version})

if __name__ == '__main__':
    app.run(debug=True)
