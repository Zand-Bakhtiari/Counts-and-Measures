#####################################################################################################################################################
# Author : Zand Bakhtiari
# Title: List MXD Data Sources
#
#
#
#####################################################################################################################################################

import arcpy, csv
arcpy.env.overwriteOutput = True


mxddoc = arcpy.GetParameterAsText(0)




layername = []
datalist = []

mxd = arcpy.mapping.MapDocument(mxddoc)
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.supports("DATASOURCE"):
        layername.append(lyr.name)   
        datalist.append(lyr.dataSource)

#%%


csvname = arcpy.GetParameterAsText(1) + ".csv"

with open(csvname, 'wb') as csvfile:
    fieldnames = ['Layer', 'Datasource']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    x = 0
    for layer in layername:
        writer.writerow({'Layer': layer, 'Datasource': datalist[x]})
        x+=1
