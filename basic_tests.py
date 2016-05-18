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
        ##closing them at once, because we won't perform any ops with
        f1.close()
        f2.close()
        f3.close()


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
    

    def tearDown (self):
    ##removing 
    #os.remove ('testsource/file1')
    #os.remove ('testsource/file2')
    #os.remove ('testsource/file3')

        shutil.rmtree ('testsource')
        shutil.rmtree('testtarget')
    

    
if __name__ == '__main__':
    unittest.main()
