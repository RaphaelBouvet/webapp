from distutils.log import debug
from turtle import title
from flask import Flask, render_template


app = Flask(__name__)
port = 5050

@app.route('/about')
def about():
    return render_template('about.html', title='ABOUT')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=port)