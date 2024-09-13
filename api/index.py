from flask import Flask, render_template
import textile

test = "is this working"


app = Flask(__name__)

@app.route('/')
def home():
    global test
    test1 = test
    return render_template('index3.html', test2=test1)

@app.route('/iocdatabase')
def database():
    return "This is the database location"
    

if __name__ == '__main__':
    app.run(debug=True)
