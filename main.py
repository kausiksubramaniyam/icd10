import icd10
import json
def icdcode_details(icdcode):
	keys=["response","code","description","billable","chapter","block","block-description"]
	details={key: None for key in keys}
	try:
		details["code"]=icdcode
		if icd10.exists(icdcode):
			details["response"]=1
			icdcode=icd10.find(icdcode)
			details["description"]=icdcode.description
			if icdcode.billable:
				details["billable"]="Yes"
			else:
				details["billable"]="No"
			details["chapter"]=icdcode.chapter
			details["block"]=icdcode.block
			details["block_description"]=icdcode.block_description
		else:
			details["response"]=0
	except ValueError:
		details["response"]=0

	json_obj=json.dumps(details,indent=4)
	return json_obj