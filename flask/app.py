from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    url = "http://fastapi-service:8000/add"
    params = {"num1": num1, "num2": num2}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        result = response.json()
        return render_template('result.html', result=result['result'])
    else:
        return "Request failed with status code {}".format(response.status_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)