__author__ = "Abhishek Shinde"
__copyright__ = "Island Exterior Fabricators LLC | EXD-AS"
__contact__ = "arabhishek1091@gmail.com | ashinde@islandcompanies.com"

"""
GOAL OF THE SCRIPT:Rename DXF for Facade Sub-assemblies received from subcontractors.

Batch Replace a string of characters from File Name's inside a folder ie Batch Renaming Files in Python
This is useful for renaming the DXF,DWG,PDF,STP,etc

This script will be integrated inside another Python Script for FRM Member Drawings
"AutoCreatesubfolders_n_movefilesndrenameRegex.py" - Work in progress
    
"""


import os

#Please change the char '\' to '\\' when you change the path
folderpath = "C:\\Users\\ashinde\\Island International Industries\\NEU - FAB TEAM - General\\On-Hold-Cut-Fins\\REL-NEU-CutFins SW & N\\BPN\\PDF"

filesin_folder = os.listdir(folderpath)
newfilenames = []
originalfilenames_withpath = []
newfilenames_withpath=[]

count = 1 

for f in filesin_folder:
    fn_withpath = os.path.join(folderpath,f)
    #.replace() is where you can change the file name pattern with names
    nfn = f.replace('_FOLDED.pdf','.pdf')
    nfn_withpath = os.path.join(folderpath,nfn)
    originalfilenames_withpath.append(fn_withpath)
    newfilenames.append(nfn)
    newfilenames_withpath.append(nfn_withpath)
    os.rename(fn_withpath,nfn_withpath)
    count += 1
    


print('\n')
print(originalfilenames_withpath)
print('\n')
print(newfilenames_withpath)


