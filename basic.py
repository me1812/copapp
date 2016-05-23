#!/usr/bin/python
import os
import shutil
import sys
import getopt

#must check if I didn't give enough parameters to the programm

class NoSuchDirectory (Exception):
    def __init__ (self, dirname):
        self.dirname = dirname
    def __str__ (self):
        return repr (self.dirname)


class NoSuchFile (Exception):
    def __init__(self, filename):
        self.filename = filename
    def __str__ (self):
        return repr (self.filename)

#def createlog (destination = )


def listDirectory (directory, fileExtList):
    '''
    takes 2 arguments:
        -- directory - full path to the directory
        -- fileExtList - [.jpg, .jpeg, .mp3, .MP3]

    return list of filepaths in format: directory/filename

    '''
    ###normalising every file path, for specific platform
    #fileNames = [os.path.normcase(f) for f in os.listdir(directory)] 
    ###for every file where extension in fileExtList-> get full path
    #filePaths = [os.path.join (directory, f) for f in fileNames\
    #if os.path.splitext(f)[1] in fileExtList]
    ##returns of list of files, with their path
    #return filePaths

    fileNames = [os.path.normcase(f) for f in os.listdir(directory)]
    filteredNames = [f for f in fileNames\
    if os.path.splitext(f)[1] in fileExtList]
    return filteredNames


def acopy (dir1, dir2, filenames):
    '''
    dir1 - source directory
    dir2 - destination directory
    filenames = a list of filenames (full paths or names
                                    blank seperator)
    if wrong filename given -> NoSuchFile exception



    '''

    ##forming a list of filepaths:
    filepaths  = []# list of full paths to files to copy

    for i in filenames:
        filepaths.append (os.path.join (dir1, i))
    
    
    ##copying each file
    for i in filepaths:
        try:
            shutil.copy2(i, dir2)
        except IOError:
            raise NoSuchFile (i)

def checkdata (dir1, dir2, filenames):
    '''
    checking for incorrect directory names

    '''
    for i in dir1, dir2:
        if os.path.exists (i) == False:
            raise NoSuchDirectory (i)

    
        

    
    


def passparam (commandline):
    '''
    takes sys.argv without a reference to the current programm
    
    getopt.getopt returns [(option, value),(option, value),]\
    [what's left]
    '''
    dir1 = commandline[0]
    print (dir1)
    dir2 = commandline[1]
    print (dir2)
    filenames = commandline[2:]
    print (filenames)
    return dir1, dir2, filenames


def framer (commandline):
    if len (commandline) < 3:
        raise TypeError
    dir1, dir2, filenames = passparam (commandline)
    checkdata (dir1, dir2, filenames)
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
    try:
        framer(sys.argv[1:])
    except NoSuchDirectory as e:
        print ("There is no such directory: ", e.dirname)

    except NoSuchFile as d:
        print ("There is no such file: ", d.filename) 
    
    except TypeError:
        print ("Please, specify source directory, target directory\
        and at least one file to copy")
