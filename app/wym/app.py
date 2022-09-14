from flask import Flask, render_template, request
from model_utils import summarize
from db_utils import connexion_db, insert_into_table, create_db

from db_utils_2 import User, get_session, verify_database, fetch_db, insert_db

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
        text_output = summarize(text_input)
        text_data = {"input_text":text_input, "output_text":text_output}
        insert_db('Text_Summ', text_data)
        return render_template('model_serve.html', summary = text_output)

if __name__ == '__main__':
    verify_database()
    app.run(debug=True, host=host, port=port)
