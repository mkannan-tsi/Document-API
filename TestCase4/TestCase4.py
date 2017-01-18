from tableaudocumentapi import Workbook
from tableaudocumentapi import Datasource
from tableaudocumentapi import Field
from tableaudocumentapi import Connection

sourceWB = Workbook('TestCase4.twbx')

db = ""
sourceDB = ""
count = 1

#Importing Datasource object from the workbook
for j in sourceWB.datasources:
	print "Datasource " + str(count)
	for x in j.connections:
		db = x.dbclass
	sourceDB = Datasource.from_connections (db, j.connections)

	#Printing information about the datasource
	print "Connection information :"
	print sourceDB.connections
	print ""
	print "Datasource caption :"
	print sourceDB.caption
	print ""
	print "Tableau version :"
	print sourceDB.version
	print ""
	sourceDB.caption = "abc"
	print sourceDB.caption
	
	#Datasource.save (sourceDB)

	#Printing information about the field
	print ""
	print "Information about fields in this order (name, id, caption, alias, datatype, role, calculation, is quantitative?, is ordinal?, is nominal?, worksheets used in, default aggregation :"
	for x in sourceDB.fields.values():
		print x.name
		print x.id
		print x.caption
		print x.alias
		print x.datatype
		print x.role
		print x.calculation
		print x.is_quantitative
		print x.is_ordinal
		print x.is_nominal
		print x.worksheets
		print x.default_aggregation
		print ""
	print ""
	print ""
	count = count+1