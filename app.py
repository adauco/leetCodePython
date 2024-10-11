from flask import Flask, render_template, request

app = Flask(__name__, static_folder="static")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    # Call your Python function here

    # For example, if you have a function called my_function in a separate Python file
    # you can call it like this:
    # from my_module import my_function
    # result = my_function()

    # The result of your function can then be passed back to the HTML page
    result = "Hola, Mundote!"

    return render_template('index.html', result=result)


@app.route('/CompareTool')
def CompareTool():
    return render_template('CompareTool.html')

@app.route('/TestCaseCreation')
def TestCaseCreation():
    return render_template('inputValues2.html')


if __name__ == '__main__':
    app.run(debug=True)
