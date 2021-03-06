####################################################################################################
# Author: Zand Bakhtiari 
# Date: September 26, 2018
#
#This script will run a query on a user defined feature dataset and find all Assets that meet the scripts criteria. It will then export the totals to a .csv spreadsheet.
#**NOTE** SQL Query need to be filled in on line #29
#
###################################################################################################
# Import modules
import arcpy, csv
arcpy.env.overwriteOutput = True




arcpy.env.workspace = arcpy.GetParameterAsText(0)

# Creates a List(fcs) of all the feature classes inteh Stormwater Feature dataset
fcs = arcpy.ListFeatureClasses()
# Sorts the fcs in alphabetical order
list.sort(fcs)
#print fcs
#%%

# Iterates over the Features in fcs and appends all of those that meet SQL query to the count list
count = []                      
for f in fcs:
    try:
        arcpy.MakeFeatureLayer_management(f, "mytableview", #SQL QUERY NEEDS TO BE SPECIFIED HERE)
        count.append(int(arcpy.GetCount_management("mytableview").getOutput(0)))
        #print count
    except RuntimeError:
        count.append("Specified Query not found")
#%%
# Create a .csv workbook that has 2 columns; one for the layer name and one for the count
csvname = arcpy.GetParameterAsText(1)

with open(csvname + ".csv", 'wb') as csvfile:
    fieldnames = ['Layer', 'Count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    x = 0
    for layer in fcs:
        writer.writerow({'Layer': layer, 'Count': count[x]})
        x+=1
