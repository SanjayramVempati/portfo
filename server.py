from flask import Flask, render_template, url_for, request
import csv


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page>')
def pagers(page):
    return render_template(page)


