from flask import Flask,render_template,request
import icd10

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def homepg():
	return render_template("ihome.html")


@app.route('/submit',methods=['GET','POST'])
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


if __name__ ==    "__main__":
	app.run(host="0.0.0.0",debug=False)
	
