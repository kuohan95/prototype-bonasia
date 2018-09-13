#!/usr/bin/python3
from flask import Flask, render_template, session as flask_session, redirect, url_for, request
import translations

app = Flask(__name__)

@app.route('/')
def home():
    # If no language is found in session, do this.
    if 'lang' not in flask_session:
        # Find out what language the browser uses and selects the most suitable
        supported_languages = ['en', 'zh']
        lang = request.accept_languages.best_match(supported_languages)
        flask_session['lang'] = lang

    if flask_session['lang'] == 'en':
        return render_template('index.html', tl=translations.En)
    if flask_session['lang'] == 'zh':
        return render_template('index.html', tl=translations.Zh)

@app.route('/lang/<lang>')
def change_lang(lang):
    flask_session['lang'] = lang
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.secret_key = 'bxbbYgl@xc5x83xd6gxf5xfax06!xa78x1b'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)