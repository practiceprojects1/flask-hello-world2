from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
  with open('final.txt', 'r') as f:
  data2 = f.read()
  return render_template('index3.html', test2=data2)

@app.route('/iocdatabase')
def database():
    return "This is the database location"
    

if __name__ == '__main__':
  url1()
  url2()
  app.run(debug=True)
