#The Order Date field has been renamed to 'abc', and contains a calculation for profit ratio.
from tableaudocumentapi import Workbook
from tableaudocumentapi import Datasource
from tableaudocumentapi import Field
from tableaudocumentapi import Connection

sourceDB = Datasource.from_file('Test.tdsx')
print "Datasource name :"
print sourceDB.name
print ""
print "Tableau version :"
print sourceDB.version
print ""
print "Connection information :"
print sourceDB.connections
print ""
sourceDB.caption = "Modified data source"
Datasource.save (sourceDB)
print "Caption post saving:"
print sourceDB.caption
print ""
#Field information that is originally commented out
#print sourceDB.fields


#Printing information about all fields
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