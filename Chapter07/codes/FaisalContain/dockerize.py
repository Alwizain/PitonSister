#!/usr/bin/env python3

# from django.shortcuts import render_template
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template('faisal.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5001"), debug=True)