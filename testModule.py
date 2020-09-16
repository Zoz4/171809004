import unittest
from tools import *
from main import *

class TestSimHash(unittest.TestCase):
    def setUp(self):
        # 设置题目给出的样例
        self.origfile = '.\\testdata\\orig.txt'
        self.imitfile_path = '.\\testdata\\'
        self.imitfile_names = ['orig.txt',
            'orig_0.8_add.txt','orig_0.8_del.txt',
           'orig_0.8_dis_3.txt','orig_0.8_dis_7.txt',
            'orig_0.8_dis_10.txt','orig_0.8_dis_15.txt',
            'orig_0.8_mix.txt','orig_0.8_rep.txt']
        print("Start testing: ")
    def tearDown(self):
        print("Test over ")

       # 进行题目中的样例测试
    def test_origData(self):
        print("测试样例数据")
        orig = SimHash( readFile(self.origfile) )
        for file_name in self.imitfile_names:
            imit = SimHash( readFile(self.imitfile_path + file_name ) )
            h = orig.hammingDistance(imit)
            print(file_name + '  Similarity: ' +str(round(1.0-h/128.0,2)) )

        # 进行自定义的样例测试
    def test_selfData1(self):

        # 选取另一篇文章（orig）和 原样例数据（other）比较 
        file_path = '.\\selfdata\\'
        orig_filename = 'orig.txt'
        imit_filename = 'other.txt'
        doSelfTest(file_path,orig_filename,imit_filename)


def doSelfTest(file_path, orig_filename, imit_filename):
    orig = SimHash( readFile( file_path+orig_filename) )
    imit = SimHash( readFile( file_path+imit_filename) )
    h = orig.hammingDistance(imit)
    print(orig_filename + ' ' + imit_filename +' Similarity: ' + str(round(1.0-h/128.0,2)) )

if __name__ == '__main__':
    unittest.main()

            


   