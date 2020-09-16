from flask import Flask ,jsonify 

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello !</h1>"


@app.route('/<myname>')
def name(myname):
    return '<h1> Hello {} !</h1>'.format(myname)

@app.route('/json')
def jsonexample():
    return jsonify({'key':'value' , 'listkey':['a', 'b', 'c', 'd']})

if __name__ == "__main__":
    app.run(debug=True)