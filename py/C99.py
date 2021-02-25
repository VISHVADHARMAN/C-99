import os
import shutil
#os.system("date")
#os.mkdir("D:/WHITEHAT JR PROJECTS AND CLASSES/PYTHON/C-99/newFolder")
os.getcwd()

#specifying path
path='D:/WHITEHAT JR PROJECTS AND CLASSES/PYTHON/C-99/C99.py'

#check whether the specified path exist or not
isExist=os.path.exists(path)
print(isExist)

#Split the path in root and ext pair
root_ext=os.path.splitext(path)

#Print root and ext of the specified path
print("Root Part: ",root_ext[0])
print("Ext Part: ",root_ext[1],"\n")

#List files and directories in the path\
path1='D:/WHITEHAT JR PROJECTS AND CLASSES/PYTHON/C-99'
print("Before Copying File: ")
print(os.listdir(path1))

#Source path
source='D:/WHITEHAT JR PROJECTS AND CLASSES/PYTHON/C-99/C99.py'

#Destination Path
destination="D:/WHITEHAT JR PROJECTS AND CLASSES/PYTHON/C-99/C99(copy).py"

#Copy the content of the source to the destination
dest=shutil.copy(source,destination)

#List files and directory after copying
print("After Copying File: ")
print(os.listdir(path1))

path2='D:/WHITEHAT JR PROJECTS AND CLASSES/PYTHON/C-99'

#List files and directories before moving file
print("Before Moving File: ")
print(os.listdir(path2))

source1='D:/WHITEHAT JR PROJECTS AND CLASSES/PYTHON/C-99/mp4'

destination1='D:/WHITEHAT JR PROJECTS AND CLASSES/PYTHON/C-99/png'

#Move the content of source1 to the destination1
dest1=shutil.move(source1,destination1)

#List files and directory after moving
print("After Moving Files: ")
print(os.listdir(path2))