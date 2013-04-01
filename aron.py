import os,re

from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/Aron')
def routeUltimateAron():
	return render_template('Aron.html')

@app.route('/Aron/googleAron', methods = ['GET','POST'])
def requestAdditionAron():
	if request.method == 'POST':
		name = request.form['name']
		return render_template('googleAron.html', name = name)
	return render_template('googleAron.html')
	
	
	
if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='127.0.0.1', port=port)