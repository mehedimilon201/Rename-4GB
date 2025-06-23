from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@mehedimilon20'


if __name__ == "__main__":
    app.run()
