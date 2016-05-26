#!/usr/bin/python
import os
import shutil #used for copying files
import sys
import getopt #not used so far
import shelve

# tuples - what are they and why they
# bolean

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

#def defaultFormats():
#    formats = [('.jpg', True),('.mp3', True),('.tex', True),('.txt', False)]
#    myShelf = shelve.open ('ext_formats.db', writeback = True)
#    myShelf['formats'] = formats
#    myShelf.close()
#    return formats
#
#def accessFormats():
#    myShelf  = shelve.open ('ext_formats.db', writeback = True)
#    try:
#        formats = myShelf['formats']
#    except:
#        formats = defaultFormats()
#    finally:
#        myShelf.close()
#        return  formats
#        
#def changeFormats(action, what):
#    formats = accessFormats()
#    if action == 'add':
#        to append = (what, True)
#        formats.append (what)
#    if action == 'delete':
#        try:
#            formatwriteFormats(formats)
#        except KeyError:
#            pass
#    writeFormats(formats)
#        
#def changeValFormats(what, how):
#    formats = accessFormats()

    
    
def defaultFormats():
    formats = {'.jpg':True,'.mp3':True,'.tex':True,'.txt':False}
    myShelf = shelve.open ('ext_formats.db', writeback = True)
    myShelf['formats'] = formats
    myShelf.close()
    return formats



def accessFormats(items_to_display = True):
    '''
    returns a list of formats that are True
    '''
    myShelf  = shelve.open ('ext_formats.db', writeback = True)
    try:
        formats = myShelf['formats']
    except:
        formats = defaultFormats()
    finally:
        myShelf.close()
        # here I should turn a dict into a list, of True valued keys
        if items_to_display == True:
            final_formats = []
            for i in formats:
                if formats[i] == True:
                    final_formats.append(i)
        if items_to_display == 'all':
            final_formats = []
            for i in formats:
                final_formats.append(i)
        #formats = formats.keys()
        if items_to_display == False:
            final_formats = []
            for i in formats:
                if formats[i] == False:
                    final_formats.append(i)
        return  final_formats

def writeFormats (new_formats):
    '''
        takes the dict
        overwrites the db
    '''
    myShelf  = shelve.open ('ext_formats.db', writeback = True)
    myShelf['formats'] = {}
    for i in new_formats:
        myShelf['formats'][i] = True
    myShelf.close()
   
################################################NOT TO USE YET

def changeFormats(action, what):
    '''
    
    '''
    myShelf  = shelve.open ('ext_formats.db', writeback = True)
    if action == 'add':
        all_keys = myShelf['formats'].keys()
        for i in what:
            if i not in all_keys:
                myShelf['formats'][i] = True
    if action == 'delete':
        try:
            myShelf['formats'].pop (what)
        except KeyError:
            pass
    myShelf.close()
###################################################
def changeValFormats(what, how):
    formats = accessFormats()
    if what in formats:
        formats[what] = how
    else:
        raise KeyError
        

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

def checkdata (dir1, dir2):
    '''
    checking for incorrect directory names

    '''
    for i in dir1, dir2:
        if os.path.exists (i) == False:
            raise NoSuchDirectory (i)

    
        

    
    


def passparam (commandline):
    '''
    takes sys.argv without a reference to the current programm
   
    used for interaction with user, checking what options are 
    passed to the programm, etc. 

    getopt.getopt returns [(option, value),(option, value),]\
    [what's left]
    '''
    dir1 = commandline[0]
    print (dir1)
    dir2 = commandline[1]
    print (dir2)
    #filenames = commandline[2:]
    #print (filenames)
    return dir1, dir2



def framer (commandline):
    '''
    for version 1.0 
    commandline arguments: dir1, dir2, files to copy
    '''
    ## checking that the script receives enough arguments
    if len (commandline) < 3:
        raise TypeError
    dir1, dir2, filenames = passparam (commandline)
    checkdata (dir1, dir2)
    acopy (dir1, dir2, filenames)




def framer1 (commandline):
    '''
    
    for version 1.1
    the programm takes source folder and target folder as args;
    chooses which files to copy according to the presaved list of
    requried FILE EXTENSIONS
    makes a copy

    KEY FUNCTIONS:
    accessFormats() - retrieves the presaved list
    listDirectory-  that makes a list of files to be copied
    
    '''
    if len (commandline) < 2:
        raise TypeError
    dir1, dir2 = passparam (commandline)
    checkdata (dir1, dir2)
    formats=accessFormats()
    fileNames = listDirectory (dir1, formats )
    acopy (dir1, dir2, fileNames)

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
        framer1(sys.argv[1:])
    except NoSuchDirectory as e:
        print ("There is no such directory: ", e.dirname)

    except NoSuchFile as d:
        print ("There is no such file: ", d.filename) 
    
    except TypeError:
        print ("Please, specify source directory, target directory\
        and at least one file to copy")
