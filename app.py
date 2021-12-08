from flask import Flask,render_template,request,redirect,url_for
from main import icdcode_details

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def homepg():
	return render_template("ihome.html")

@app.route('/icd-extraction',methods=['POST','GET'])
def disp():
	icdcode=request.json['icdcode']
	try:
		return icdcode_details(icdcode)
	except ModuleNotFoundError:
		return "Unable to find module."
if __name__ ==    "__main__":
	app.run(host="0.0.0.0",debug=False)