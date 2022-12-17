from flask import Flask, render_template, request
from db import dbResult, dbResultParam
from query import *

import platform
app = Flask(__name__)


@app.route("/")
def main():
    res = dbResult(allMovie)
    romance = dbResultParam(topGenre, "Romance")
    adventure = dbResultParam(topGenre, "Adventure")
    thriller = dbResultParam(topGenre, "Thriller")
    return render_template('index.html', res = res,
                            romance=romance,
                            adventure=adventure,
                            thriller=thriller  )


@app.route("/movie/<id>")
def detail(id): 
    res = dbResultParam(movieDetail, id)
    movie = dbResultParam(recommentMoive, id)
    return render_template('single.html', res = res, movie=movie)

if __name__ == "__main__":
     # Check the System Type before to decide to bind
     # If the system is a Linux machine -:) 
    if platform.system() == "Linux":
        app.run(host='0.0.0.0',port=5000, debug=True)
     # If the system is a windows /!\ Change  /!\ the   /!\ Port
    elif platform.system() == "Windows":
        app.run(host='0.0.0.0',port=50000, debug=True)