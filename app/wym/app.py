from flask import Flask, render_template, request
from model_utils import summarize
from db_utils_2 import User, get_session, verify_database, fetch_db, insert_db, get_db
import matplotlib.pyplot as plt
import datetime
import time

app = Flask(__name__)
port = 5050
host = '0.0.0.0'

@app.route('/')
def home():
    return render_template('home.html', title='HOME')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contacted', methods=['POST'])
def contacted():
    if request.method == 'POST':
        user_data = request.form
        print(f'User_data :{user_data}')
        print(type(user_data))
        insert_db('User', user_data)
        return render_template('contacted.html', result=user_data["name"])

@app.route('/model',  methods= ['POST', 'GET'])
def model():
    if request.method == 'GET':
        return render_template('model.html')
    elif request.method == 'POST':
        text_input = request.form['texte']
        print(f'TEXT INPUT {text_input}')
        text_output, time_treated = summarize(text_input)
        text_data = {
            "input_text" : text_input, 
            "output_text" : text_output,
            "time_treated" : time_treated}
        insert_db('Text_Summ', text_data)
        return render_template('model_serve.html', summary = text_output)

@app.route('/mario')
def mario():
    iframe="http://127.0.0.1:8600/"
    return render_template('mario.html', iframe=iframe)

@app.route('/dash')
def dash():
    query = get_db()
    mean_time = 0 
    for q in query:
        mean_time += q.time
    mean_time /= len(query)
    return render_template('dash.html', model_param=mean_time)


if __name__ == '__main__':
    verify_database()
    app.run(debug=True, host=host, port=port)
