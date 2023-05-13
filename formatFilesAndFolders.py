import os
from pathlib import Path
import shutil

#getCurrentDirectoy
print(os.getcwd())

#changeCurrentDirectory
os.chdir('C:/Users/Hp/Pictures/CameraRoll')
print(os.getcwd())

#getListOfAllFilesInDirectory (even hidden files & folders)
print(os.listdir())

#getNameExtensionOfFiles
for index, file in enumerate(os.listdir()): #using an index variable while looping through array requires 'enumerate' keyword
    name, extension = os.path.splitext(file)
    print(name)
    print(extension)
    
    #renameFiles
    newName = f"image-{str(index).zfill(3)}{extension}" #zfill makes sure to keep required number of digits in a string by adding necessary 0s at start
    os.rename(file, newName)


#createNewFolderInCurrentDirectory
Path('data').mkdir(exist_ok=True) #name of folder is 'data', exist_ok=True will create the folder even if it already exists
"""
if not os.path.exists("data"):
    os.mkdir("data")   
"""


#moveFileToAnotherFolder
for file in os.listdir():
    if file == 'data':
        continue
    shutil.move(file, "data")
    

#copyPasteFileToAnotherFolder
for file in os.listdir():
    if file == 'data':
        continue
    shutil.copy(file, "data")
    shutil.copy2(file, "data") #if we want to keep the same meta data as the ones for previous files

#removeFile
os.remove("filename")

#removeFolder
os.rmdir("folderName") #only if folder is empty
shutil.rmtree("folderName") #if folder is not empty & has some files in  it
