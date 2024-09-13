from flask import Flask, render_template

test = ""

def test():
    global test
    test = test+"test"



app = Flask(__name__)

@app.route('/')
def home():
    global test
    return render_template('index2.html', test1=test)
    

if __name__ == '__main__':
    test()
    app.run(debug=True)
