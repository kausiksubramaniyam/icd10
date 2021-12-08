from flask import Flask,render_template,request,redirect,url_for
import main

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def homepg():
	return render_template("ihome.html")

@app.route('/submit',methods=['POST','GET'])
def disp():
	icdcode=request.form['icdcode']
	try:
		return code_details(icdcode)
	except ModuleNotFoundError:
		return "Unable to find module."
if __name__ ==    "__main__":
	app.run(host="0.0.0.0",debug=False)