#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return f'{text}'

@app.route('/count/<num>')
def count(num):
    return '\n'.join([str(x) for x in range(int(num))]) + '\n'
    # return '\n'.join(str(x) for x in range(num))

@app.route('/math/<int:num1>/<op>/<int:num2>')
def math(num1, op, num2):
    if op == '+':
        return f'{num1 + num2}'
    elif op == '-':
        return f'{num1 - num2}'
    elif op == '*':
        return f'{num1 * num2}'
    elif op == 'div':
        return f'{num1 / num2}'
    elif op == '%':
        return f'{num1 % num2}'
        

if __name__ == '__main__':
    app.run(port=5555, debug=True)
