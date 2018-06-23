from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello, world! I'm a minimal Flask app hosted with Apache + mod_wsgi."
 
if __name__ == "__main__":
    app.run()