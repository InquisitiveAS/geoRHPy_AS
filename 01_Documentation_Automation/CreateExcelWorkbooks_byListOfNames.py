__author__ = "Abhishek Shinde"
__copyrights__ = "EXD-AS | ashinde at IslandExteriorFabricatorsLLC(IEF) "
__contact__ = "arabhishek1091@gmail.com | ashinde@umich.edu"

"""
GOAL: Create Bunch of Workbooks given a List of File Names
This is typically used in creating Bill of Materials for missing BOM for given Materials
Using the filename string from the filetypes(.pdf,.dxf,.csv,etc) provided for Materials
we can create a blank Workbooks based on the Material's filename using string method manipulation

In this example below we are creating BOM ( .xlsx file's) for parts which have PDF's
"""

import os
from openpyxl import Workbook

fileNamesFolder = os.listdir("C:\\Users\\ashinde\\Island International Industries\\NEU - FAB TEAM - General\\On-Hold-Cut-Fins\\REL-NEU-CutFins_NE_&_SE\\ASM.F\\PDF")
filesSavePath = "C:\\Users\\ashinde\\Island International Industries\\NEU - FAB TEAM - General\\On-Hold-Cut-Fins\\REL-NEU-CutFins_NE_&_SE\\ASM.F\\BOM"
filenames =[]

for f in fileNamesFolder:
    new_f = f.strip('.pdf')
    filenames.append(new_f)
    wb = Workbook()
    ws = wb.active
    #ws_custom = wb.create_sheet("Sheet1")
    wbFilesSavePath = filesSavePath + '\\' + new_f + ".xlsx"
    print(wbFilesSavePath)
    wb.save(wbFilesSavePath)
    
#print(filenames)

