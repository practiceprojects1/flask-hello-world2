from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')

def text():
    return "This is test text"

if __name__ == '__main__':
    app.run(debug=True)
