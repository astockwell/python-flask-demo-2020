from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details', methods=['POST', 'GET'])
def details():
    error = None
    if request.method == 'POST':
        print(request.form['email'])
        print(request.form['answer'])
        if request.form['email'] == "" or request.form['answer'] == "":
            return render_template('details.html', error="Email and Answer are required fields")

        return redirect("/")

    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('details.html', error=error)