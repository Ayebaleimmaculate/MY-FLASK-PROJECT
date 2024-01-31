from flask import Flask

app = Flask(__name__)


from flask import render_template
# Home page
@app.route('/')
def home():
    return render_template('home.html')
    '<h1>Welcome to Immy and Daughter liquide soap company</h1>' 

# addational routes
@app.route('/about')
def about():
    return render_template('about.html')
    '<h2>Description about the company</h2>'

@app.route('/contact')
def contact():
    return render_template('contact.html')
    '<h3> You can reach us via Email:nisimaimmy@gmial.com or by phone at +25675846558</h3>'

# route with parameter
@app.route('/user/<username>')
def user(username):
    return '<p>Hello, hope all is going on well with and we are glad to serve you.</p>'

# Displaying a personalized greeting
@app.route('/user/<username>')
def greet_user(username):
    return f'hello, {username}! Welcome to our website.'

from flask import request
#route for the form submission
@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method =="POST":
        #retrive data from the form
        name = request.form.get('name')
        email = request.form.get('email')
        #returning aresponse acknowledging the submission
        return f'Thank you, {name}, for submitting your email: {email}!'
    else:
        #render the form template for GET request
        return render_template('submit_form.html')



