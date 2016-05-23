import basic
import unittest
import os
import shutil

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
        ##opening a number of files to copy

        f1 = open ('testsource/file1', 'w')
        f2 = open ('testsource/file2', 'w')
        f3 = open ('testsource/file3', 'w')
        ##########################################files with ext
        f4 = open ('testsource/file4.txt', 'w')
        f5 = open ('testsource/file5.jpg', 'w')
        f6 = open ('testsource/file6.mp3', 'w')
        ##########################################files one dir up
        os.mkdir ('../testsource1')
        os.mkdir ('../testtarget1')
        f7 = open ('../testsource1/outerfile1.txt', 'w')
        f8 = open ('../testsource1/outerfile2.jpg', 'w')
        f9 = open ('../testsource1/outerfile3.mp3', 'w')
        


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
    def testAcopy4 (self):
        pass

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

    def tearDown (self):
    ##removing 
    #os.remove ('testsource/file1')
    #os.remove ('testsource/file2')
    #os.remove ('testsource/file3')

        shutil.rmtree ('testsource')
        shutil.rmtree('testtarget')
        shutil.rmtree ('../testsource1')
        shutil.rmtree ('../testtarget1')
    

    
if __name__ == '__main__':
    unittest.main()
