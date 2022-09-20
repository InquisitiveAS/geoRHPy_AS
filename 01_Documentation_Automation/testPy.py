__author__ = "EXD-AS | ashinde |Abhishek Shinde"
__contact__ = "arabhishek1091@gmail.com | ashinde@umich.edu"

#GOAL: A Python file imported as module inside GH | Rhino 
#      Function inside this python file will open a text file and write data inside this python file
#PSEUDOCODE:-
#It consists of Function test which will open a text file (user provided file-path)
#The function test will open the text file and write data inside it.
#After writing succesfully the function will display the file path

import os

def test():
    path = "C:\\Users\\ashinde\\OneDrive - Island International Industries\\Desktop\\CD_AS_IEF\\PythonDevelopment_AS_IEF\\externalPy\\test.txt"
    with open (path, 'w') as file: 
        file.write ("Text file was opened successfully and data to write is:" + "\n" + "GH told me to execute this")
    if os.path.isfile(path):
        return path
    else:
    	return None
