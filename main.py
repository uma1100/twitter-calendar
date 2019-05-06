import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template, request
import requests
import getfavoritelist as fav



app = Flask(__name__)

# @app.route('/')
# def hello():
#     return render_template('form.html')

@app.route('/',methods=["GET","POST"])
def twifav():
	if request.method == "POST":
		screen_name = request.form['screen_name']
		data = fav.get_list(screen_name)
		# data = "test"
		return render_template('index.html',data=data,name=screen_name)
	else:
		screen_name = None
		data = None
		return render_template('index.html',data=data,name=screen_name)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)