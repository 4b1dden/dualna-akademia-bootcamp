import flask

app = flask.Flask(__name__)

@app.route('/')
def main():
    return 'Ahoj Svet!'

@app.route('/pozdrav')
def pozdrav():
    return 'Ahoj!'

@app.route('/pozdrav/<meno>')
def pozdrav_meno(meno):
    return 'Ahoj, ' + meno + "!"
    
app.run()