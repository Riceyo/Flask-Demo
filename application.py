from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	#return('blah')
	return render_template('bender.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
