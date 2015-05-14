from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/demo1/')
def demo1_1():
	return '<h1>hello,world!</h1>'


@app.route("/demo1/demo1_2/")
def demo1_2():
	user_agent=request.headers.get('User-Agent')
	return '<h1>your browser is %s </h1>' % user_agent

@app.route('/demo1/<name>')
def demo1_3(name):
	return '<h1>hello,%s!</h1>' % name

if __name__ =='__main__':
	app.run(debug=True)