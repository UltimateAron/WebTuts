import os,re,math
from time import gmtime, strftime

from flask import Flask,render_template,request,session,g,redirect, url_for,abort, flash

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


# Static routing
# Please check the files ending in .html in the templates folder to understand about rendering template.
@app.route('/TheEngineer') # Replace TheEngineer with your nickname
def routeStaticTheEngineer():
	imageURL = 'http://placehold.it/350x150&text=imageOne'
	return render_template('TheEngineer.html', imageURL=imageURL)


"""
HitmanFoo # Static routing, static files and return render_template



"""
"""
biscuit # Static routing, static files and return render_template



"""
"""
aronLim # Static routing, static files and return render_template

@app.route('/UltimateAron')									
def routeStaticUltimateAron():								
	return render_template ('UltimateAron.html')			

"""

# Dynamic routing
@app.route('/TheEngineer/<int:visitor>')
def routeDynamicTheEngineer(visitor):
	numOfVisitor = visitor
	return render_template('DynamicTheEngineer.html', numOfVisitor=numOfVisitor)
"""
HitmanFoo # Dynamic routing



"""
"""
biscuit # Dynamic routing



"""
"""
aronLim # Dynamic routing

@app.route('/UltimateAron/<int:x>')
def routeDynamicUltimateAron(x):							
	powerToPower = math.pow(x,x)							
	return render_template ('DynamicUltimateAron.html',awesomeness = powerToPower)	

"""


# HTTP methods
# N.B: The default method is GET. If no method is defined, Flask will think that it should execute GET.
@app.route('/TheEngineer/HTTPmethods',methods=['GET', 'POST'])
def httpMethodsTheEngineer():
	if request.method == 'POST':
		# if client/browser is requesting a POST method then execute this.
		varTheEngineer = 1 + 2
		return render_template('HTTPmethodsTheEngineer.html', varTheEngineer = varTheEngineer)
	if request.method == 'GET':
		varTheEngineer = 1 + 1
		return render_template('HTTPmethodsTheEngineer.html', varTheEngineer = varTheEngineer)
"""
HitmanFoo # Dynamic routing



"""
"""
biscuit # Dynamic routing



"""
"""
aronLim # Dynamic routing

@app.route('/UltimateAron/HTTPmethods',methods=['GET','POST'])
def httpMethodsUltimateAron():
	if request.method == 'GET':								#if client(browser) is requesting for GET method, then execute the function.
		varUltimateAron = 1*2
		return render_template('HTTPmethodsUltimateAron.html',varUltimateAron = varUltimateAron)
	if request.method == 'POST':
		varUltimateAron = 2*3
		return render_template('HTTPmethodsUltimateAron.html',varUltimateAron = varUltimateAron)

"""

# RequestData
@app.route('/TheEngineer/requestData',methods=['GET', 'POST'])
def requestDataTheEngineer():
	if request.method == 'POST':
		name = request.form['name']
		location = request.form['location']
		return render_template('requestDataTheEngineer.html', **locals())
	return render_template('requestDataTheEngineer.html')
"""
HitmanFoo # Request Data



"""
"""
biscuit # Request Data



"""
"""
aronLim # Request Data

"""

@app.route('/UltimateAron/requestData',methods=['GET', 'POST'])
def requestDataUltimateAron():
	if request.method == 'POST':
		username = request.form['username']
		location = request.form['location']
		return render_template('requestDataUltimateAron.html', **locals())
	return render_template('requestDataUltimateAron.html')



# Session & url_for & flash
# App secret should be stored in the configuration section
app.secret_key = 'ultimate/123Aron/345Killed/456Hitman/987Foo/432By/543Eating/435Biscuit'

@app.route('/TheEngineer/storeSession')
def storeSessionTheEngineer():
	session['timeEntered'] = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
	flash('Data stored in session & you have been redirected to index page')
	return redirect(url_for('index'))

@app.route('/TheEngineer/checkSession')
def checkSessionTheEngineer():
	checkSession = session['timeEntered']
	return render_template('checkSessionTheEngineer.html', checkSession=checkSession)

@app.route('/TheEngineer/popSession')
def popSessionTheEngineer():
	session.pop('timeEntered', None)
	flash('Data removed from session & you have been redirected to index page')
	return redirect(url_for('index'))
"""
HitmanFoo # Session



"""
"""
biscuit # Session



"""
"""
aronLim # Session



"""



if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='127.0.0.1', port=port)





