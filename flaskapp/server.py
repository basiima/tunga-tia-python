from flask import Flask
app = Flask(__name__)

# route for "/"
@app.route('/')
def hello_world():
    return "Hello Julius"

# route for "/about"
@app.route('/about')
def about():
    return "About page"

if __name__ == '__main__':
    app.run()
        