import os, fnmatch
import os

def match(fld, search):
    for file in os.listdir(fld):
        if fnmatch.fnmatch(file, search):
            print(file)

            
match("./11 Files Handling", "*.txt")
print(os.getcwd())