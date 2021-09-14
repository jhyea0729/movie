from flask import Flask
from flask.templating import render_template
import movie_api as ma


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", movies = ma.callMovieApi(), temps = ma.callTempApi()) # default가 1이라서 안넣어도 1로 된다. 

if __name__ == "__main__":
    app.run(debug=True)