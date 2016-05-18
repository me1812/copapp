#!/usr/bin/python
import os
import shutil
import sys
import getopt


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
        filepaths.append (os.path.join (dir1, i))
    
    
    ##copying each file
    for i in filepaths:
        shutil.copy2(i, dir2)


def passparam (commandline):
    '''
    takes sys.argv without a reference to the current programm
    
    getopt.getopt returns [(option, value),(option, value),]\
    [what's left]
    '''
    print (commandline)
    
    data = getopt.getopt (commandline, 'a')
    print (data[1])
    return (data[1])
    
if __name__ == "__main__": 
    print (sys.argv)
    passparam (sys.argv[1:])

    
    
