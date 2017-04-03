from flask import Flask,redirect,url_for
from flask import request
from flask import flash
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/bus_pass_renewal'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

@app.route('/')
def login():
  return render_template("login.html")

 
@app.route('/login_reg',methods=['GET','POST'])
def login_reg():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    
    register= registration.query.filter_by(username=username,password=password).first()
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
		return redirect(url_for('addbus'))
	
    if register is None:
        return redirect(url_for('login'))
    return redirect(url_for('success',username=username))
    #elif request.form['password'] == 'password' and request.form['username'] == 'admin':
		#return redirect(url_for('operatorview'))
	#else:
		#flash('wrong password')
	 #return redirect(url_for('login'))
#@app.route('/delete/<int:id>',method=['POST'])
#def remove(id):
 #       object=object.query.get_or_404(id)
  #      delete(object)	
	#	return redirect('busdetails')
  
@app.route('/remove/<int:id>', methods=['POST'])
def remove(id):
    
    addbusid = addbus.query.get(id)
    db.session.delete(addbusid)
    db.session.commit()
    return redirect(url_for('busdetails'))
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    
    register = registration.query.get(id)
    db.session.delete(register)
    db.session.commit()
    return redirect(url_for('userdetails'))
		
@app.route('/register')
def home_register():
		return render_template('register.html')
		
@app.route('/studentview')
def studentview():
  return render_template("studentview.html")
@app.route('/verification')
def verification():
  return render_template("verification.html")

@app.route('/applypass')
def applypass():
	return render_template("applypass.html")    
@app.route('/operatorview')
def operatorview():
	return render_template("operatorview.html")    
 
@app.route('/passrenewal')
def passrenewal():
	return render_template("renewal.html")   
@app.route('/changepassword')
def changepassword():
	return render_template("changepassword.html")   
@app.route('/addbus')
def addbus():
	return render_template("addbus.html")   
@app.route('/editbus')
def editbus():
	return render_template("editbus.html")   
@app.route('/mail')
def mail():
	return render_template("mail.html")   
@app.route('/userdetails')
def userdetails():
  return render_template("userdetails.html",registration=registration.query.all())
@app.route('/busdetailss')
def busdetailss():
  return render_template("busdetailss.html",addbus=addbus.query.all())

@app.route('/busdetails')
def busdetails():
  return render_template("busdetails.html",addbus=addbus.query.all())

@app.route('/payment')
def payment():
	return render_template("payment.html")  
@app.route('/generatepass')
def generatepass():
	return render_template("generatepass.html")  
	 
@app.route('/sucess/<username>')
def success(username):
	return render_template('studentview.html',registration=registration.query.filter_by(username='%s'%username))  
	
@app.route('/verifysuccess/<username>')
def verifysuccess(username):
	return render_template('payment.html',passregister=passregister.query.filter_by(username='%s'%username))  
@app.route('/verifyrenewal/<username>')
def verifyrenewal(username):
	return render_template('paymentrenewal.html',passrenewal=passrenewal.query.filter_by(username='%s'%username))  

@app.route('/paymentsucess/<username>')
def paymentsucess(username):
	return render_template('generatepass.html',passregister=passregister.query.filter_by(username='%s'%username))  
@app.route('/paymentrenewal/<username>')
def paymentrenewal(username):
	return render_template('generaterenewal.html',passrenewal=passrenewal.query.filter_by(username='%s'%username))  

	
     
 
class registration(db.Model):
	id = db.Column('register_id', db.Integer, primary_key = True )
	username=db.Column(db.String(50),unique=True)
	password=db.Column(db.String(50),unique=True)
	phone = db.Column(db.Integer)
	gender=db.Column(db.String(50))
	age = db.Column(db.Integer)
	address=db.Column(db.String(50))
	email=db.Column(db.String(50),unique=True)
	college=db.Column(db.String(50))
	course=db.Column(db.String(50))
	department=db.Column(db.String(50))
	
	
	
	
	
	def __init__(self,username,password,phone,gender,age,address,email,college,course,department):
		self.username=username
		self.password=password
		self.phone=phone
		self.gender=gender
		self.age=age
		self.address=address
		self.email=email
		self.college=college
		self.course=course
		self.department=department
			
				
	@app.route('/register', methods = ['GET', 'POST'])
	def register():
		if request.method == 'POST':
			if not request.form['username'] or not request.form['password'] or not request.form['phone'] or not request.form['gender'] or not request.form['age'] or not request.form['address'] or not request.form['email'] or not request.form['college'] or not request.form['course'] or not request.form['department']:
					flash('Please enter all the fields', 'error')
			else:
				register = registration(request.form['username'],request.form['password'],request.form['phone'],request.form['gender'],request.form['age'],request.form['address'],request.form['email'],request.form['college'],request.form['course'],request.form['department'] )          
				db.session.add(register)
				db.session.commit()
				flash('Record was successfully added')
			return redirect(url_for('login'))
		return render_template('register.html') 
		
class passregister(db.Model):
	id = db.Column('passregisterid_id', db.Integer, primary_key = True )
	username=db.Column(db.String(50),unique=True)
	locationstart=db.Column(db.String(50))
	locationend=db.Column(db.String(50))
	result = db.Column(db.Integer)
	ttf = db.Column(db.Integer)
	datestart= db.Column(db.Date)
	dateend= db.Column(db.String(50))
	address=db.Column(db.String(100))
	email=db.Column(db.String(50),unique=True)
	college=db.Column(db.String(50))
	course=db.Column(db.String(50))
	department=db.Column(db.String(50))
	
	
	
	
	
	def __init__(self,username,locationstart,locationend,result,ttf,datestart,dateend,address,email,college,course,department):
		self.username=username
		self.locationstart=locationstart
		self.locationend=locationend
		self.result=result
		self.ttf=ttf
		self.datestart=datestart
		self.dateend=dateend
		self.address=address
		self.email=email
		self.college=college
		self.course=course
		self.department=department
		
			
				
	@app.route('/pass_register', methods = ['GET', 'POST'])
	def pass_register():
		if request.method == 'POST':
			if not request.form['username'] or not request.form['locationstart'] or not request.form['locationend'] or not request.form['result'] or not request.form['ttf'] or not request.form['datestart'] or not request.form['dateend'] or not request.form['address'] or not request.form['email'] or not request.form['college'] or not request.form['course'] or not request.form['department'] :
					flash('Please enter all the fields', 'error')
			else:
				passregisterid = passregister(request.form['username'],request.form['locationstart'],request.form['locationend'],request.form['result'],request.form['ttf'],request.form['datestart'],request.form['dateend'],request.form['address'],request.form['email'],request.form['college'],request.form['course'],request.form['department'])          
				namee=request.form['username']
				
				db.session.add(passregisterid)
				db.session.commit()
				flash('Record was successfully added')
				
			return redirect(url_for('verifysuccess',username=namee))
		return render_template('applypass.html') 
		
class passrenewal(db.Model):
	id = db.Column('passrenewalid_id', db.Integer, primary_key = True )
	username=db.Column(db.String(50),unique=True)
	locationstart=db.Column(db.String(50))
	locationend=db.Column(db.String(50))
	result = db.Column(db.Integer)
	ttf = db.Column(db.Integer)
	datestart= db.Column(db.Date)
	dateend= db.Column(db.String(50))
	
	
	
	
	
	def __init__(self,username,locationstart,locationend,result,ttf,datestart,dateend):
		self.username=username
		self.locationstart=locationstart
		self.locationend=locationend
		self.result=result
		self.ttf=ttf
		self.datestart=datestart
		self.dateend=dateend
			
				
	@app.route('/pass_renewal', methods = ['GET', 'POST'])
	def pass_renewal():
		if request.method == 'POST':
			if not request.form['username'] or not request.form['locationstart'] or not request.form['locationend'] or not request.form['result'] or not request.form['ttf'] or not request.form['datestart'] or not request.form['dateend']:
					flash('Please enter all the fields', 'error')
			else:
				passrenewalid = passrenewal(request.form['username'],request.form['locationstart'],request.form['locationend'],request.form['result'],request.form['ttf'],request.form['datestart'],request.form['dateend'])          
				namee=request.form['username']
				
				db.session.add(passrenewalid)
				db.session.commit()
				flash('Record was successfully added')
				
			return redirect(url_for('verifyrenewal',username=namee))
		return render_template('renewal.html') 
		
class addbus(db.Model):
	id = db.Column('addbusid_id', db.Integer, primary_key = True )
	busnumber=db.Column(db.Integer)
	locationstart=db.Column(db.String(50))
	locationend=db.Column(db.String(50))
	stopa=db.Column(db.String(50))
	stopb=db.Column(db.String(50))
	stopc=db.Column(db.String(50))
	stopd=db.Column(db.String(50))
	stope=db.Column(db.String(50))
	stopf=db.Column(db.String(50))
	stopg=db.Column(db.String(50))
	
	
	
	
	
	def __init__(self,busnumber,locationstart,locationend,stopa,stopb,stopc,stopd,stope,stopf,stopg):
		self.busnumber=busnumber
		self.locationstart=locationstart
		self.locationend=locationend
		self.stopa=stopa
		self.stopb=stopb
		self.stopc=stopc
		self.stopd=stopd
		self.stope=stope
		self.stopf=stopf
		self.stopg=stopg
			
	

			

			
	
				
	@app.route('/add_bus', methods = ['GET', 'POST'])
	def add_bus():
		if request.method == 'POST':
			if not request.form['busnumber'] or not request.form['locationstart'] or not request.form['locationend'] or not request.form['stopa'] or not request.form['stopb'] or not request.form['stopc'] or not request.form['stopd'] or not request.form['stope'] or not request.form['stopf']  or not request.form['stopg'] :
					flash('Please enter all the fields', 'error')
			else:
				addbusid = addbus(request.form['busnumber'],request.form['locationstart'],request.form['locationend'],request.form['stopa'],request.form['stopb'],request.form['stopc'],request.form['stopd'],request.form['stope'],request.form['stopf'],request.form['stopg'])          
				db.session.add(addbusid)
				db.session.commit()
				flash('Record was successfully added')
				
				
			return redirect(url_for('addbus'))
		return render_template('addbus.html') 

class payment(db.Model):
	id = db.Column('paymentid_id', db.Integer, primary_key = True )
	username=db.Column(db.String(50))
	cardnumber=db.Column(db.Integer)
	amount=db.Column(db.Integer)
	cvv=db.Column(db.Integer)
	expirydate=db.Column(db.Date)
	
	
	
	
	
	def __init__(self,username,cardnumber,amount,cvv,expirydate):

		self.username=username
		self.cardnumber=cardnumber
		self.amount=amount
		self.cvv=cvv
		self.expirydate=expirydate
				
	
				
	@app.route('/payment_verify', methods = ['GET', 'POST'])
	def payment_verify():
		if request.method == 'POST':
			if not request.form['username'] or not request.form['cardnumber'] or not request.form['amount'] or not request.form['cvv'] or not request.form['expirydate'] :
					flash('Please enter all the fields', 'error')
			else:
				paymentid = payment(request.form['username'],request.form['cardnumber'],request.form['amount'],request.form['cvv'],request.form['expirydate'])          
				namee=request.form['username']
				db.session.add(paymentid)
				db.session.commit()
				flash('Record was successfully added')
				
				
			return redirect(url_for('paymentsucess',username=namee))
		return render_template('payment.html') 


class paymentrenewal(db.Model):
	id = db.Column('paymentid_id', db.Integer, primary_key = True )
	username=db.Column(db.String(50))
	cardnumber=db.Column(db.Integer)
	amount=db.Column(db.Integer)
	cvv=db.Column(db.Integer)
	expirydate=db.Column(db.Date)
	
	
	
	
	
	def __init__(self,username,cardnumber,amount,cvv,expirydate):

		self.username=username
		self.cardnumber=cardnumber
		self.amount=amount
		self.cvv=cvv
		self.expirydate=expirydate
				
	
				
	@app.route('/payment_renewal', methods = ['GET', 'POST'])
	def payment_renewal():
		if request.method == 'POST':
			if not request.form['username'] or not request.form['cardnumber'] or not request.form['amount'] or not request.form['cvv'] or not request.form['expirydate'] :
					flash('Please enter all the fields', 'error')
			else:
				paymentid = payment(request.form['username'],request.form['cardnumber'],request.form['amount'],request.form['cvv'],request.form['expirydate'])          
				namee=request.form['username']
				db.session.add(paymentid)
				db.session.commit()
				flash('Record was successfully added')
				
				
			return redirect(url_for('paymentrenewal',username=namee))
		return render_template('payment.html') 

if __name__ == '__main__':
	   db.create_all()
	   app.run(debug=True)
  







