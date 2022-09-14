from flask import Flask, render_template, request
from model_utils import summarize
from db_utils import connexion_db, insert_into_table, create_db

from db_utils_2 import User, get_session, verify_database, fetch_db

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

# @app.route('/contacted',  methods= ['POST'])
# def contacted():
#     if request.method == 'POST':
#         form = request.form
#         result_form = []
#         result_form.append(form['name'])
#         result_form.append(form['mail'])
#         result_form.append(form['phone'])
#         result_form.append(form['comment'])
#         print(result_form)

#         curs = connexion_db()
#         create_db(curs, "app_v_r_d")
#         insert_into_table(curs, result_form)
#         return render_template('contacted.html', result=result_form[0])

@app.route('/contacted', methods=['POST'])
def contacted():
    if request.method == 'POST':
        user_data = request.form
        print(f'User_data :{user_data}')
        user = User(**user_data)
        session = get_session()
        session.add(user)
        session.commit()
        return render_template('contacted.html', result=user.name)

@app.route('/model',  methods= ['POST', 'GET'])
def model():
    if request.method == 'GET':
        return render_template('model.html')
    elif request.method == 'POST':
        text_input = request.form['texte']
        print(f'TEXT INPUT {text_input}')
        text_output = summarize(text_input)
        return render_template('model_serve.html', summary = text_output[0])

if __name__ == '__main__':
    verify_database()
    app.run(debug=True, host=host, port=port)
