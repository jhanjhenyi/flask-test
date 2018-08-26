from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<num1>/<num2>')
def show_multiply_result(num1, num2):
    result = ''

    try:
        result = str(int(num1) * int(num2))
    except ValueError:
        result = 'only int is accepted'

    return result


if __name__ == '__main__':
    app.run(debug=True)
