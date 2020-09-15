import unittest
from tools import *

class TestSimHash(unittest.TestCase):
    def setUp(self):
        self.origfile = '.\\testdata\\orig.txt'
        self.imitfile_path = '.\\testdata'
        self.imitfile_names = ['orig.txt',
            'orig_0.8_add.txt','orig_0.8_del.txt',
           'orig_0.8_dis_3.txt','orig_0.8_dis_7.txt',
            'orig_0.8_dis_10.txt','orig_0.8_dis_15.txt',
            'orig_0.8_mix.txt','orig_0.8_rep.txt',
            'other.txt']
        print("Start testing: ")
    def tearDown(self):
        print("Testing over ")
    def test_data(self):
        orig = SimHash( readFile(self.origfile) )
        for file_name in self.imitfile_names:
            imit = SimHash( readFile(self.imitfile_path + '\\' + file_name ) )
            h = orig.hammingDistance(imit)
            print(file_name + ' Similarity: ' +str(round(1-h/128.0,2)) )

if __name__ == '__main__':
    unittest.main()

            


   