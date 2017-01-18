from tableaudocumentapi import Workbook
from tableaudocumentapi import Connection

sourceWB = Workbook('TestCase3.twbx')

#Allowing the user to choose whether to replace the datasource with an embedded or published connection
user_login = ""
print "The workbook is currently connected to a flat file and a published datasource but can be replaced by an alternative embedded or published connection respectively. The embedded connection will fail due to differences in table names but the published connection will not. The published connection can be found in the Presales site. Choose the type of datasource you would like to replace the existing connection with : "
user_login = raw_input ("Please enter your demoapac.tableau.com username: ")

#Replacing the datasource connection details
for x in sourceWB.datasources:
	for j in x.connections:
		if j.dbclass != "sqlproxy":
 			j.server = "sql.databender.net, 14333"
 			j.dbname = "Superstore"
 			j.dbclass = "sqlserver"
 			j.username = "alan"

		elif j.dbclass == "sqlproxy":
 			j.server = "https://demoapac.tableau.com"
 			j.dbname = "TestCase3-destination"
 			j.username = "alan"

#Saving the workbook
Workbook.save_as (sourceWB, 'TestCase3 output.twbx')

print ""
print "The workbook connections have been updated. Please open the newly created workbook to test."