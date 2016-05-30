import basic
import unittest
import os
import shutil
import shelve

class TestClasses (unittest.TestCase):

    ''' creating files to copy.
    names: file1,file2, file3
    open them, then close at once to create
    remove them at teardown
    '''
    def setUp (self):

        ## creating source and target directories
        os.mkdir ('testsource')
        os.mkdir ('testtarget')
        #####################################################
        ##opening a number of files to copy

        f1 = open ('testsource/file1', 'w')
        f2 = open ('testsource/file2', 'w')
        f3 = open ('testsource/file3', 'w')
        ##########################################files with ext
        f4 = open ('testsource/file4.txt', 'w')
        f5 = open ('testsource/file5.jpg', 'w')
        f6 = open ('testsource/file6.mp3', 'w')
        f10 = open ('testsource/file10.tex', 'w')
        ##########################################files one dir up
        os.mkdir ('../testsource1') #creating a dir above current
        os.mkdir ('../testtarget1')
        f7 = open ('../testsource1/outerfile1.txt', 'w')
        f8 = open ('../testsource1/outerfile2.jpg', 'w')
        f9 = open ('../testsource1/outerfile3.mp3', 'w')
        

        ############################################################# 
        ##closing them at once, because we won't perform any ops with
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
        f6.close()
        f7.close()
        f8.close()
        f9.close()



    def testFirst (self):
        self.assertTrue (os.path.exists ('testsource'))
        self.assertTrue (os.path.exists ('testtarget'))
        self.assertTrue (os.path.exists ('testsource/file1'))
        self.assertTrue (os.path.exists ('testsource/file2'))
        self.assertTrue (os.path.exists ('testsource/file3'))
        self.assertFalse (os.path.exists ('blah/blahblah'))


    '''
    copies from dir1 to dir 2;
    both dirs exist and are subdirs of cwe
    all files exist
    '''
    def testAcopy1 (self):
        basic.acopy ('testsource', 'testtarget', ['file1',\
        'file2', 'file3'])
        self.assertTrue (os.path.exists ('testtarget/file1'))
        self.assertTrue (os.path.exists ('testtarget/file2'))
        self.assertTrue (os.path.exists ('testtarget/file3'))
   

        
    
    '''
    both dirs exist and are subdirs of cwe
    a full path to the file is given, not a name
    '''
    def testAcopy2 (self):
        basic.acopy ('testsource', 'testtarget',\
        ['/home/dragonpython/projects/my_applications/copapp/testsource/file5.jpg'])
        self.assertTrue (os.path.exists ('testtarget/file5.jpg'))

    #'''
    #both dirs exist and are subdirs of cwe
    #a directory/name format path to the file is given, not a name
    #logically, doesn't work this way
    #'''
    #def testAcopy3 (self):
    #    basic.acopy ('testsource', 'testtarget', ['testsource/file1'])
    #    self.assertTrue (os.path.exists ('testtarget/file1'))
        

    '''
    both dirs exist and are one directory above cwe
    '''

    def testListDirectory1 (self):
        result = basic.listDirectory ('testsource', ['.jpg', '.mp3'])
        if 'testsource/file5.jpg' in result:
            self.assertTrue
        if 'testsource/file6.mp3' in result:
            self.assertTrue
        self.assertEqual (len(result), 2)


    '''
    files in the above cwd directory
    '''
    def testListDirectory2 (self):
        result = basic.listDirectory ('../testsource1', ['.jpg', '.mp3'])

        if '../testsource1/file5.jpg' in result:
            self.assertTrue
        if '../testsource1/file6.mp3' in result:
            self.assertTrue
        self.assertEqual (len(result), 2)

    '''
    basic connection with acopy
    '''
    def testListDirectory3 (self):
        result = basic.listDirectory ('testsource', ['.jpg', '.mp3'])
        basic.acopy ('testsource','testtarget',  result)
        self.assertTrue (os.path.exists ('testtarget/file5.jpg'))
        self.assertTrue (os.path.exists ('testtarget/file6.mp3'))
        self.assertFalse (os.path.exists ('testtarget/file4.txt'))


    '''
    checking the proper creation of db and dictionary
    '''
    def testdefaultFormats1 (self):
        formats, nonformats = basic.defaultFormats()
        
        self.assertTrue (os.path.exists ('ext_formats.db'))


        myShelf = shelve.open ('ext_formats.db')
        
        if 'formats' in myShelf:
            self.assertTrue

        if 'nonformats' in myShelf:
            self.assertTrue
        
        default =\
        {'.jpg':True,'.mp3':True,'.tex':True,'.txt':False}
        
        #for i in default if i in myShelf['formats'].keys())
        for i in default:
            self.assertTrue ( i in myShelf['formats'].keys())

    '''
    there is no presaved list- generating default
    '''
    def testaccessFormats1 (self): 
        formats = basic.accessFormats()

        default = ['.jpg','.mp3','.tex']
        for i in default:
            self.assertTrue (i in formats)

        self.assertEqual (len(formats), len(default))


    '''
    there is a presaved list - should return all its True valued keys

    creating presaved list manually
    '''
    def testaccessFormats2 (self):

        myShelf = shelve.open ('ext_formats.db', writeback=True)

        default =\
        {'.jpg':True,'.mp3':True,'.tex':True,'.txt':False}

        myShelf['formats'] = default

        myShelf.close()

        self.testaccessFormats1()

        #formats = basic.accessFormats()

        #default = ['.jpg','.mp3','.tex']
        #for i in default:
        #    self.assertTrue (i in formats)

        #self.assertEqual (len(formats), len(default))


        #myShelf.close()

    '''

    there is a presaved list - should return all its True valued keys

    creating presaved list with basic.defaultFormats()
    '''
    def testaccessFormats3 (self):
        formats = basic.defaultFormats()
        self.testaccessFormats1()
        

    '''
    overwriting existing file
    '''
    def testWriteFormats1(self):
        myShelf = shelve.open ('ext_formats.db', writeback=True)

        default =\
        {'.jpg':True,'.mp3':True,'.tex':True,'.txt':False}

        new = \
        {'.avi':True,'.mpeg':True,'.doc':True,'.adoc':False}
        myShelf['formats'] = default

        myShelf.close()

        basic.writeFormats (new)

        myShelf = shelve.open ('ext_formats.db', writeback=True)
        formats = myShelf['formats']
        myShelf.close()
        
        for i in new:
            self.assertTrue (i in formats)

        self.assertEqual (len(formats), len(new))

        
    '''
    writing list anew
    '''
    def testWriteFormats2(self):

        new = \
        {'.avi':True,'.mpeg':True,'.doc':True,'.adoc':False}


        basic.writeFormats (new)

        myShelf = shelve.open ('ext_formats.db', writeback=True)
        formats = myShelf['formats']
        myShelf.close()
        
        for i in new:
            self.assertTrue (i in formats)

        self.assertEqual (len(formats), len(new))

    '''
    checking that tearDown works properly with ext_formats.db 
    '''
    def testdefaultFormats2 (self):
        
        self.assertFalse (os.path.exists ('ext_formats.db'))

       
    '''
    no preexisting extentions list
        f4 = open ('testsource/file4.txt', 'w')
        f5 = open ('testsource/file5.jpg', 'w')
        f6 = open ('testsource/file6.mp3', 'w')
        f10 = open ('testsource/file10.tex', 'w')
    formats = {'.jpg':True,'.mp3':True,'.tex':True,'.txt':False}
    '''
    def testframer11 (self):
        basic.framer1 (['testsource', 'testtarget'])
        self.assertTrue (os.path.exists ('testtarget/file5.jpg'))
        self.assertTrue (os.path.exists ('testtarget/file6.mp3'))
        self.assertTrue (os.path.exists ('testtarget/file10.tex'))
        self.assertFalse (os.path.exists('testtarget/file4.txt'))
        self.assertEqual (len(os.listdir('testtarget')), 3)
       

    '''
    adding a new extension
    '''
    def testChangeFormats (self):

        basic. defaultFormats()
        basic.changeFormats ('add', ['.avi'])

        myShelf = shelve.open ('ext_formats.db')
        formats = myShelf['formats'].keys()
        myShelf.close()
       
        ##checking complete list in the extlist
        supposed = ['.jpg','.mp3','.tex', 'txt', 'avi']

        self.assertTrue ('.jpg' in formats)
        self.assertTrue ('.mp3' in formats)
        self.assertTrue ('.tex' in formats)
        self.assertTrue ('.txt' in formats)
        self.assertTrue ('.avi' in formats)

        self.assertEqual (len(formats), len(supposed))

    #    ## checking that correct values are True

        

        

    def tearDown (self):
    ##removing 
    #os.remove ('testsource/file1')
    #os.remove ('testsource/file2')
    #os.remove ('testsource/file3')

        shutil.rmtree ('testsource')
        shutil.rmtree('testtarget')
        shutil.rmtree ('../testsource1')
        shutil.rmtree ('../testtarget1')
        
        try: #that is, if there is such a file
            os.remove ('ext_formats.db')
        except:
            pass

    
if __name__ == '__main__':
    unittest.main()
