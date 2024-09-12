from flask import Flask, render_template

app = Flask(__name__, static_folder='api/static')

@app.route('/')
def home():
    return render_template('templates/index2.html')

if __name__ == '__main__':
    app.run(debug=True)
