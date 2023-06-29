from flask import Flask, jsonify
from flask_restful import Resource, Api, request
import pyodbc 
from datetime import date
import pandas as pd

# Input Parameters
getdatacmd='SELECT id AS EmployeeId, name AS Name, designation AS Designation, location AS Location FROM Employees'
connstring='DRIVER={ODBC Driver 18 for SQL Server};SERVER=LHR-5CG04932TD\SQLEXPRESS;DATABASE=demo;ENCRYPT=no;Trusted_Connection=yes;'
today=date.today().strftime('%d.%m.%Y')
filename='exported_data'+today+'.xlsx'

# Create the flask app
app = Flask(__name__)
# Create an API object
api = Api(app)

# Class for GetData
class GetData(Resource):
	# GET Request
	def get(self):
		args = request.args
		cnxn = pyodbc.connect(connstring)
		sql_query = pd.read_sql_query( getdatacmd,cnxn)
		df = pd.DataFrame(sql_query)
		df = df.assign(Date = today, Code=args['code'])
		df.to_excel(filename, index = False)
		return filename + ' is exported successfully'
		
# Add the defined resources along with their corresponding urls
api.add_resource(GetData, '/')

# Driver function
if __name__ == '__main__':

	app.run(debug = True)
