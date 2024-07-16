from flask import Flask,redirect,url_for
from flask import render_template


app=Flask(__name__)
@app.route("/") 



def home():
    return render_template('index.html')


if __name__ == "__main__":
    #Run the app in decorator mode
    app.run(debug=True)