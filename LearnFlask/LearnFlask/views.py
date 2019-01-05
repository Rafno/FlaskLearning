"""
Routes and views for the flask application.
"""
from io import BytesIO
from datetime import datetime
from flask import render_template, send_file, make_response
from LearnFlask import app
from .classes.Planet import Planet

planet = Planet()

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

@app.route('/mars')
def about():
    """Renders the about page."""
    planet.set_name('Mars')
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message=planet.introduction()
    )

@app.route('/jupyter')
def test():
    planet.set_name('Jupyter')
    """Renders the test page."""
    return render_template(
        'testing.html',
        title='Testing',
        year=datetime.now().year,
        message=planet.introduction()
    )