from flask import Flask

app = Flask(__name__)

@app.route('/')

# index page created
@app.route('/index/')

# hell world phrase created
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/about/')
def about():
    return '<h3>About Us.</h3>'

@app.route('/contact/')
def contact():
    return '<h3>To contact, please email Layne.Johnson@stonybrook.edu.</h3>'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

