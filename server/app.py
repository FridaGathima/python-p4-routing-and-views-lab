#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print (parameter)
    return parameter

@app.route('/count/<number>')
def count(number):
    count = ""
    for i in range(int(number)):
        count += f'{i}' + "\n"
    return count

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):

    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    return str(result)
    
