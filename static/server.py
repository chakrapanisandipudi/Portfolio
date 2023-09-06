import csv
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def about_us(page_name):
    return render_template(page_name)

# @app.route('/contact/')
# def contact_us():
#     return render_template('contact.html')

# @app.route('/food/')
# def food():
#     return render_template('food.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_file(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv_writer(database2, delimiter=',', new_line='', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/thanku.html')
    else:
        return 'Something went wrong please check'
