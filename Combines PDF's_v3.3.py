"""
author = "ashinde"
copyright = "Island Consolidated LLC"
date_created = "08032021"

This script combines StoryPole tickets for Facade SubAssembly Fabrication with PNL tickets from the subcontractors

"""

import os
from PyPDF2 import PdfFileMerger,PdfFileReader

#Note:When you paste file path in Visual Studio 9,replace the \ with  \\
folder1 = "C:\\Users\\ashinde\\Island International Industries\\NEU - FAB TEAM - General\\Fin Storypole\\L01-07 and L01-7I temp pdf"
folder2 = "C:\\Users\\ashinde\\OneDrive - Island International Industries\\Desktop\\Abhishek Sept-Oct2021\\NEU Project Panel Tickets\\L01-07\\Fabrication Tickets"
merged_folder = "C:\\Users\\ashinde\OneDrive - Island International Industries\\Desktop\\Abhishek Sept-Oct2021\\NEU Project Panel Tickets\\L01-07\\Output Folder"

f1_files = os.listdir(folder1)
#folder1 contains ['PID-NEU-XX-00-000.0.pdf','PID-NEU-XX-00-000.0.pdf',...etc]-PDF's with FIN Names
f2_files = os.listdir(folder2)
#folder2 contains ['PNL-NEU-0000-X0+PID-NEU-XXX.pdf','PNL-NEU-0000-X0+PID-NEU-XXX.pdf',...etc]-CADMAKERS PNL PDFs copied and renamed from GH Script
#folder2 files to be renamed as ['PNL-NEU-0000-X0-PID-NEU-XX-00-000.0.pdf'] using GH script

#as = PdfFileReader(file)

def pdf_merger(f2,f1):
    merger = PdfFileMerger()
    f1_content = PdfFileReader(open(os.path.join(folder1,f1),'rb'))
    f2_content = PdfFileReader(open(os.path.join(folder2,f2),'rb'))
    merger.append(f2_content)
    merger.append(f1_content)
    out = os.path.join(merged_folder,f"{f1.strip('.pdf')}+{f2}")
    merger.write(out)

"""
Below code will iterate each file in folder1 and checks if those in folder2 filename string 'FNN-PID-01.pdf'
contains substring 'PID-01.pdf'. if matches, the 2 matching files are merged and saved to merged folder
"""
for file1 in f1_files:
    for file2 in f2_files:
        if len(file2.strip('.pdf')) > 16 :            
            if file2.split('+')[1].strip('.pdf') == file1.strip('.pdf'):
                print(file1.strip(".pdf") + '+' + file2.split('+')[0].strip('.pdf'))
                #print(file2.strip('.pdf') + "  +  " + file1.strip('.pdf'))
                pdf_merger(file2,file1)

