from flask import Flask, render_template

test = ""

def test():
    global test
    test = test+"testTESTTESTTEST"



app = Flask(__name__)

@app.route('/')
def home():
    global test
    test1=print(test)
    return render_template('index2.html', test2=test1)
    

if __name__ == '__main__':
    test()
    app.run(debug=True)
