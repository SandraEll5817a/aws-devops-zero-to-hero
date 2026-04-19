from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/health')
def health():
    return 'OK', 200

@app.route('/version')
def version():
    return {'version': '1.0.0', 'app': 'simple-python-app'}, 200

if __name__ == '__main__':
    # Disabled debug mode for safer local testing
    app.run(host='0.0.0.0', port=5000, debug=False)
