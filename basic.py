#!/usr/bin/python
import os
import shutil
import sys
import getopt


#class NoSuchDirectory (Exception):
#    def __init__ (self, dirname):
#        self.dirname = dirname
#    def __str__ (self):
#        return repr (self.value)







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

#def checkdata (dir1, dir2, filenames):
#
#    ##checking for incorrect directory names
#    for i in dir1, dir2:
#        if os.path.exists (i) == False:
#            raise NoSuchDirectory (i)

    
        

    
    


def passparam (commandline):
    '''
    takes sys.argv without a reference to the current programm
    
    getopt.getopt returns [(option, value),(option, value),]\
    [what's left]
    '''
    dir1 = commandline[0]
    dir2 = commandline[1]
    filenames = commandline[2:]
    return dir1, dir2, filenames


def framer (commandline):
    dir1, dir2, filenames = passparam (commandline)
    acopy (dir1, dir2, filenames)
    ####################################################getopt
    #data = getopt.getopt (commandline, 'a')
    #print data
    #dir1 = data[1][0]
    #dir2 = data[1][1]
    #filenames = data[2:]# here is a mistake connected with slicing
    #print (dir1)
    #print (dir2)
    #print (filenames)
    #return dir1, dir2, filenames
    ################################################################
if __name__ == "__main__": 
    framer(sys.argv[1:])


    
    
