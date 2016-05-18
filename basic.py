import os
from shutil import copy2

#print (os.getcwd())
#


def getfilepath (somedir, filename):
    result = os.path.join (somedir, filename)
    return result


'''
dir1 - source directory
    - in some cases can be current directory
dir2 - destination directory
filenames = a list of strings
'''
def acopy (dir1, dir2, filenames):

    #forming a list of filepaths:
    filepaths  = []
    for i in filenames:
        filepaths.append (getfilepath(dir1, i))
    
    print (filepaths)
    
    #copying each file

    

    
    
