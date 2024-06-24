from flask import render_template, redirect, url_for, flash
from test import app

@app.route('/')
def home():
    return "<h1>Hello world</h1>"