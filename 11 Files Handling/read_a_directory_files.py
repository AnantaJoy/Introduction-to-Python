import os

# Read a directory files
DIRECTORY_PATH = "./11 Files Handling"

def directory(files):
    for file in os.listdir(files):
        if file.endswith(".txt"):
            print(file)

directory(DIRECTORY_PATH)


# Search for files in a directory
def directory(files, search):
    for file in os.listdir(files):
        if file.endswith(search):
            print(file)

directory(DIRECTORY_PATH, ".csv")


# Search for file names
def directory(files, search):
    for file in os.listdir(files):
        if file.startswith(search):
            print(file)

directory("./11 Files Handling", "names")