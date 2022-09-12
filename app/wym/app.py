from flask import Flask, render_template, request


app = Flask(__name__)
port = 5050

@app.route('/')
def home():
    return render_template('home.html', title='HOME')

@app.route('/about')
def about():
    return render_template('about.html', title='ABOUT')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/model',  methods= ['POST', 'GET'])
def model():
    if request.method == 'GET':
        return render_template('model.html')
    elif request.method == 'POST':
        text_input = request.form
        print(text_input)
        return render_template('model_serve.html', summary = text_input)

if __name__ == '__main__':
    app.run(debug=True, port=port)
