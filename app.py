from flask import Flask,render_template,request,redirect,url_for
import icd10

app=Flask(__name__)

@app.route('/home')
@app.route('/')
def homepg():
	return render_template("ihome.html")


@app.route('/submit',methods=['POST'])
def disp():
	icdcode=request.form['icdcode']
	if icd10.exists(icdcode):
		code=icd10.find(icdcode)
		if code.billable:
		    a="billable"
		else:
			a="not billable"

		return render_template("ihome2.html",icdcode=icdcode,desc=code.description,bill=a,chapter=code.chapter,block=code.block,bdesc=code.block_description)
	else:
		return render_template("ihome.html",k="Invalid Code, Please Retry!")

#desc=code.description,bill=a,chapter=code.chapter,block=code.block,bdesc=code.block_description)

if __name__ ==    "__main__":
	app.run(debug=True)