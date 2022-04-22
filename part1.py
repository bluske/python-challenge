import requests
import pandas as pd

pd.set_option('display.float_format','{:.0f}'.format)

api = "https://reqres.in/api/products/"

ID = "id"
NAME = "name"
YEAR = "year"
COLOR = "color"
PANTONE_VAL = "pantone_value"

products = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 500, 501]

dataFrame = {
	ID: [],
	NAME: [],
	YEAR: [],
	COLOR: [],
	PANTONE_VAL: []
}

for i, pid in enumerate(products):

	res = requests.get(api + str(pid)).json()

	if 'data' in res:
		data = res["data"]
		dataFrame[ID].append(data[ID])
		dataFrame[NAME].append(data[NAME])
		dataFrame[YEAR].append(data[YEAR])
		dataFrame[COLOR].append(data[COLOR])
		dataFrame[PANTONE_VAL].append(data[PANTONE_VAL])
	else:
		dataFrame[ID].append(pid)
		dataFrame[NAME].append(None)
		dataFrame[YEAR].append(None)
		dataFrame[COLOR].append(None)
		dataFrame[PANTONE_VAL].append(None)

df = pd.DataFrame(dataFrame)

df[YEAR] = df[YEAR].replace([2010], 2099)

print(df)

median = df[YEAR].median()
medianStr = ('%f' % median).rstrip('0').rstrip('.')

print('\nMedian year of product is {} \n'.format(medianStr))