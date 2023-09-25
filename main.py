from flask import Flask,render_template,url_for

app = Flask(__name__)

#the home page 
@app.route("/")
def home():
  return render_template('home.html')

@app.route("/aboutus")
def aboutus():
  return render_template('aboutus.html')

@app.route("/home1")
def home1():
  return render_template('index.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
  