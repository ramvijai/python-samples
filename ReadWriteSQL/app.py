from flask import Flask, jsonify
from flask_restful import Resource, Api
import pyodbc 

# Input Parameters
getdatacmd='SELECT id, column1, column2 FROM Source'
connstring='DRIVER={ODBC Driver 18 for SQL Server};SERVER=LHR-5CG04932TD\SQLEXPRESS;DATABASE=sample;ENCRYPT=no;Trusted_Connection=yes;'

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
			results.append(value)	
			cursor.execute('INSERT INTO Target (id, column1, column2) values(?,?,?)', value['id'],value['column1'],value['column2'])		
		cnxn.commit()
		cursor.close() 
		return jsonify({'message': 'The below specified data added to database'},{'data': results} ) 
				

# Add the defined resources along with their corresponding urls
api.add_resource(GetData, '/')

# Driver function
if __name__ == '__main__':

	app.run(debug = True)