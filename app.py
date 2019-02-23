from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return 'Helloooooooo......'

@app.route("/home")
def home():
    return 'my home page'

if(__name__=="__main__"):
    app.run()