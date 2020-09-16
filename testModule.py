import unittest
from tools import *

class TestSimHash(unittest.TestCase):
    def setUp(self):
        print("Start testing: ")
    def tearDown(self):
        print("Test over ")

       # 进行题目中的样例测试
    def test_origData1(self):
        doSelfTest('.\\testdata\\','orig.txt','orig.txt')
    def test_origData2(self):
        doSelfTest('.\\testdata\\','orig.txt','orig_0.8_add.txt')
    def test_origData3(self):
        doSelfTest('.\\testdata\\','orig.txt','orig_0.8_del.txt')
    def test_origData4(self):
        doSelfTest('.\\testdata\\','orig.txt','orig_0.8_dis_3.txt')
    def test_origData5(self):
        doSelfTest('.\\testdata\\','orig.txt','orig_0.8_dis_7.txt')
    def test_origData6(self):
        doSelfTest('.\\testdata\\','orig.txt','orig_0.8_dis_10.txt')
    def test_origData7(self):
        doSelfTest('.\\testdata\\','orig.txt','orig_0.8_dis_15.txt')
    def test_origData8(self):
        doSelfTest('.\\testdata\\','orig.txt','orig_0.8_mix.txt')
    def test_origData9(self):
        doSelfTest('.\\testdata\\','orig.txt','orig_0.8_rep.txt')

       # 进行自定义的样例测试
    def test_selfData1(self):
        # 选取另一篇文章（orig）和 原样例数据（other）比较 
        doSelfTest('.\\selfdata\\','orig.txt','other.txt')

def doSelfTest(file_path, orig_filename, imit_filename):
    orig = SimHash( readFile( file_path+orig_filename) )
    imit = SimHash( readFile( file_path+imit_filename) )
    h = orig.hammingDistance(imit)
    print(orig_filename + '  ' + imit_filename +'  Similarity: ' + str(round(1.0-h/128.0,2)) )

if __name__ == '__main__':
    unittest.main()

            


   