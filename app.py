import os
from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
    return "Welcome to CICD demo online test"
@app.route("/gcp")
def gcp():
    return "welcome to GCP, Amazing"
if __name__ == "__main__":

    app.run(host='0.0.0.0', port=int('8001'))
