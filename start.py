from flask import Flask,render_template,request
from combinations import *
app = Flask(__name__)
 
@app.route('/')
def form():
    if request.method == 'GET':
        return render_template('form.html')
 
@app.route('/result/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /result is accessed directly. Try going to '/' to submit form"

    if request.method == 'POST':
        form_data = request.form
        number=[]
        for key, value in request.form.items():
            number.append (int(value))

        return render_template('data.html',your_list = combination(number))
 
if __name__ == "__main__":
    app.run(host='localhost', port=5000)