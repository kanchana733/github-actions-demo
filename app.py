# app.py — Flask API for GitHub Actions CI demo
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'version': '1.0.0'})

@app.route('/square/<int:n>')
def square(n):
    return jsonify({'input': n, 'result': n * n})

@app.route('/greet/<name>')
def greet(name):
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route('/sum/<int:a>/<int:b>')
def sum_nums(a, b):
    return jsonify({'result': a + b})
#Add a very long comment line that exceeds the character limit to intentionally trigger a lint violation.Return to your Pull Request on GitHub and watch the check turn into a red cross. Take a screenshot here for your lab manual to show how the CI pipeline blocks faulty code.After taking your screenshot, remove the long line from app.py, save, and push the fix again:

