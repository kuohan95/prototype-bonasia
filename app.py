#!/usr/bin/python3
from flask import Flask, render_template, session as flask_session, redirect, url_for
import translations

app = Flask(__name__)

@app.route('/')
def home():
    # Redirects the user if no language is stored in session
    if 'lang' not in flask_session:
        return redirect(url_for('choose_lang'))

    if flask_session['lang'] == 'en':
        return render_template('index.html', tl=translations.En)
    if flask_session['lang'] == 'zh':
        return render_template('index.html', tl=translations.Zh)

@app.route('/choose_lang')
def choose_lang():
    return render_template('choose_lang.html')

@app.route('/lang/<lang>')
def change_lang(lang):
    flask_session['lang'] = lang
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.secret_key = 'bxbbYgl@xc5x83xd6gxf5xfax06!xa78x1b'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)