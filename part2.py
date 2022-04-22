from flask import request, Flask
from flask_cors import CORS
from datetime import datetime
import requests

api = "https://reqres.in/api/products/"

app = Flask(__name__)
CORS(app)

@app.route('/product/<pid>', methods=['GET'])
def get_product_info(pid):
	insert_db = request.args.get('insert_db') == 'true'
	if pid.isnumeric():
		product = int(pid)
		if product < 5:
			return get_original_json(product, insert_db)
		else:
			return get_without_support_json(product, insert_db)
	else:
		return '', 405

def get_original_json(pid, insert):
	res = requests.get(api + str(pid)).json()
	if insert:
		res['Uploaded_db'] = db_datetime()
	return res

def get_without_support_json(pid, insert):
	res = requests.get(api + str(pid)).json()
	if 'data' in res:
		res.pop('support', None)
		res["data"]["EVALUATION"] = "TESTING"
		if insert:
			res['Uploaded_db'] = db_datetime()
		return res
	else:
		return { "id": pid, "note": "No data available"}

def db_datetime(): 
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3001)

