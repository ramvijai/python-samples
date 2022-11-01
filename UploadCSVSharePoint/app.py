from flask import Flask
from flask_restful import Resource, Api
import pyodbc
from datetime import date
from io import BytesIO
import pandas as pd
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential


# Input Parameters
getdatacmd = 'SELECT id AS EmployeeId, name AS Name, designation AS Designation, location AS Location FROM Employees'
connstring = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=LHR-5CG04932TD\SQLEXPRESS;DATABASE=demo;ENCRYPT=no;Trusted_Connection=yes;'
today = date.today().strftime('%d.%m.%Y')
sharepoint_url = 'https://v2technologies683.sharepoint.com/sites/Demo'
clientid = '18e1fecc-0925-4372-ae38-53471502998a'
clientsecret = 'gTvLMjA1Mt32zErA0XmZQjlX4ANWsfsN6nrYplIF2zg='
relative_url = f'Demo'
filename = r'Employees_SQL_'+today+'.csv'

# Create the flask app
app = Flask(__name__)
# Create an API object
api = Api(app)

# Class for UploadCSVToSharePoint
class UploadCSVToSharePoint(Resource):
	# GET Request
	def get(self):
        # Read data from SQL table
		cnxn = pyodbc.connect(connstring)
		sql_query = pd.read_sql_query(getdatacmd, cnxn)
		df = pd.DataFrame(sql_query)
		
        # Connect to SharePoint
		client_credentials = ClientCredential(clientid, clientsecret)		
		ctx = ClientContext(sharepoint_url).with_credentials(client_credentials)		
		target_folder = ctx.web.get_folder_by_server_relative_url(relative_url)

		# Create a buffer object
		buffer = BytesIO()  

		# Write the dataframe to the buffer            
		df.to_csv(buffer, index=False)
		buffer.seek(0)
		file_content = buffer.read()

        # Upload the file			
		target_file = target_folder.upload_file(filename, file_content).execute_query()		
		return 'File has been uploaded to url: {0}'.format(target_file.serverRelativeUrl)	      
        
# Add the defined resources along with their corresponding urls
api.add_resource(UploadCSVToSharePoint, '/')

# Driver function
if __name__ == '__main__':

	app.run(debug = True)
