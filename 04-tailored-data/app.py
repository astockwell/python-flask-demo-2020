from flask import Flask, render_template, redirect, request
app = Flask(__name__)

direct_reports = {
    'astockwell': {'directs': ['stockwell\'s minion #1', 'stockwell\'s minion #1']},
    'ktyers': {'directs': ['tyers\'s minion #1', 'tyers\'s minion #1']},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details', methods=['POST', 'GET'])
def details():
    error = None
    if request.method == 'POST':
        print(request.form['email'])
        if request.form['email'] in direct_reports:
            return redirect('/details/{}'.format(request.form['email']))
        error = "Email not found"

    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('details.html', error=error)

@app.route('/details/<username>')
def profile(username):
    return render_template('direct_reports.html', direct_reports=direct_reports[username]['directs'])