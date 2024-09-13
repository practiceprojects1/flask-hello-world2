from flask import Flask, render_template
import textile

test = ""

def test():
    global test
    test = test+"testTESTTESTTEST"



app = Flask(__name__)

@app.route('/')
def home():
    global test
    test1=test
    html = textile.textile(test1)
    return render_template('index2.html', test2=html)
    

if __name__ == '__main__':
    test()
    app.run(debug=True)
