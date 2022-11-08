from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("html/index.html")

if __name__ == "__main__":
    app.run(debug=True)