from flask import Flask, render_template

with open('final.txt', 'r') as f:
  data2 = f.read()
  f.close()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index3.html', test2=data2)

@app.route('/iocdatabase')
def database():
    return "This is the database location"
    

if __name__ == '__main__':
  url1()
  url2()
  app.run(debug=True)
