from flask import  Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello world</h1>"

@app.route("/h2")
def hello_world2():
    return "<h1> hello 2 world </h1>"

@app.route("/test2")
def test2():
    data = request.args.get('x')
    return 'this is the data u input in the url{}'.format(data)

if __name__ == "__main__":
    app.run(host = "0.0.0.0")

