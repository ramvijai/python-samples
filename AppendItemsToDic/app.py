from flask import Flask, jsonify
from flask_restful import Resource, Api, request
import pyodbc 
from datetime import date

# Input Parameters
getdatacmd='SELECT id AS EmployeeId, name AS Name, designation AS Designation, location AS Location FROM Employees'
connstring='DRIVER={ODBC Driver 18 for SQL Server};SERVER=LHR-5CG04932TD\SQLEXPRESS;DATABASE=demo;ENCRYPT=no;Trusted_Connection=yes;'
today=date.today().strftime('%d.%m.%Y')

# Create the flask app
app = Flask(__name__)
# Create an API object
api = Api(app)

# Class for GetData
class GetData(Resource):
	# GET Request
	def get(self):        
		cnxn = pyodbc.connect(connstring)
		cursor = cnxn.cursor()
		cursor.execute(getdatacmd)	
		columns = [column[0] for column in cursor.description]
		results = []	
		rows = cursor.fetchall()
		for row in rows:
			value=dict(zip(columns, row))					
			value.update({'Date': today})
            # Get the values from query parameter
            # /?code='<value>'
			value.update({'Code': request.args['code']})		
			results.append(value)		
		return jsonify({'data': results})

# Add the defined resources along with their corresponding urls
api.add_resource(GetData, '/')

# Driver function
if __name__ == '__main__':

	app.run(debug = True)
