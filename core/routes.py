from datetime import datetime
from core.models import ShortUrls
from core import app, db
from random import choice
import string
from urllib.parse import urlparse
from flask import render_template, request, flash, redirect, url_for


def generate_short_id(num_of_chars: int):
    """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))


@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        url = request.form['url']
        short_id = request.form['custom_id']

        # Ensure that the custom short ID isn't already in use
        if short_id and ShortUrls.query.filter_by(short_id=short_id).first() is not None:
            flash('That\'s already in use! Please enter different custom id.')
            return redirect(url_for('index'))

        # Ensure there is a URL entered
        if not url:
            flash('The URL is required! Don\'t leave this blank.')
            return redirect(url_for('index'))

        # Ensure that the URL isn't malformed or not a URL
        if uri_validator(url) == False:
            flash('This doesn\'t look like a valid URL!')
            return redirect(url_for('index'))

        if not short_id:
            short_id = generate_short_id(8)

        new_link = ShortUrls(
            original_url=url, short_id=short_id, created_at=datetime.now())
        db.session.add(new_link)
        db.session.commit()
        short_url = request.host_url + short_id

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False

@app.route('/<short_id>')
def redirect_url(short_id):
    link = ShortUrls.query.filter_by(short_id=short_id).first()
    if link:
        return redirect(link.original_url)
    else:
        flash('Invalid URL')
        return redirect(url_for('index'))