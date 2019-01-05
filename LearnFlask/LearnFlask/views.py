"""
Routes and views for the flask application.
"""
from io import BytesIO
from datetime import datetime
from flask import render_template, send_file, make_response
from LearnFlask import app


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/test')
def test():
    """Renders the test page."""
    return render_template(
        'testing.html',
        title='Testing',
        year=datetime.now().year,
        message='This page was made for testing purposes'
    )