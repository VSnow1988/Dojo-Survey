from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")
app.run(debug=True)

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    favlang = request.form['favlang']
    comment = request.form['comment']
    print request.form
    return redirect('/submit')
app.run(debug=True)

@app.route('submit')
def display():
    return render_template("submitted.html")
app.run(debug=True)
