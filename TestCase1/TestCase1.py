from tableaudocumentapi import Workbook
from tableaudocumentapi import Connection

sourceWB = Workbook('TestCase1.twbx')

#Printing workbook information
print "Workbook Name : " 
print sourceWB.filename
print "Sheet Names : " 
print sourceWB.worksheets

#Printing data connection information
for x in sourceWB.datasources:
	print "Datasource details in following order (Server name, database name, user name, database type, port, authentication) :"
	for j in x.connections:
 		print j.server
 		print j.dbname
 		print j.username
 		print j.dbclass
 		print j.port
 		print j.authentication
 		print " "