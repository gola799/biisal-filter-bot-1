from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Jai Shree Krishna !"
if __name__ == "__main__":
    app.run()
