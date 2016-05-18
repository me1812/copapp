import os
from shutil import copy2

#print (os.getcwd())
#




'''
dir1 - source directory
    - in some cases can be current directory
dir2 - destination directory
filenames = a list of filenames


'''
def acopy (dir1, dir2, filenames):

    ##forming a list of filepaths:
    filepaths  = []# list of full paths to files to copy
    for i in filenames:
        filepaths.append (os.path.join (dir1, i)
    
    
    ##copying each file
    for i in filepaths:
        shutil.copy2(i, dir2)


    

    
    
