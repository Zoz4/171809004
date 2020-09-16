import unittest
from tools import *
import os
from main import *
import warnings

class TestSimHash(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print("\nStart testing: ")
    def tearDown(self):
        print("Test over\n")

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

       # 选取另一篇文章（orig）和 原样例数据（other）比较 
    def test_selfData1(self):
        doSelfTest('.\\selfdata\\','orig.txt','other.txt')
    # 测试main.py
       # os.chdir(文件 main.py 所在目录) 
    # 正常执行
    def test_main(self):
       os.chdir('.\\')
       os.system('python main.py .\\selfdata\\orig.txt .\\selfdata\\other.txt .\\selfdata\\result.txt' )
    def test_mainerror1(self):
       # 原文件名（路径）错误
       os.chdir('.\\')
       os.system('python main.py .\\selfdata\\a.txt .\\selfdata\\orig.txt .\\selfdata\\result.txt' )
    def test_mainerror2(self):
       # 抄袭文件名（路径）错误
       os.chdir('.\\')
       os.system('python main.py .\\selfdata\\orig.txt .\\selfdata\\a.txt .\\selfdata\\result.txt' )
    def test_mainerror3(self):
       # 目的文件名（路径）错误
       os.chdir('.\\')
       os.system('python main.py .\\selfdata\\orig.txt .\\selfdata\\other.txt .\\error\\result.txt' )
    # 空文件错误
    def test_mainerror4(self):
       # 原文件为空
       os.chdir('.\\')
       os.system('python main.py .\\selfdata\\empty.txt .\\selfdata\\orig.txt .\\selfdata\\result.txt' )
    def test_mainerror5(self):
       # 抄袭文件为空
       os.chdir('.\\')
       os.system('python main.py .\\selfdata\\orig.txt .\\selfdata\\empty.txt .\\selfdata\\result.txt' )
    def test_mainerror6(self):
       # TF-IDF得到键值对字典为空
       os.chdir('.\\')
       os.system('python main.py .\\selfdata\\sign.txt .\\selfdata\\orig.txt .\\testdata\\result.txt' )

def doSelfTest(file_path, orig_filename, imit_filename):
    orig = SimHash( readFile( file_path+orig_filename) )
    imit = SimHash( readFile( file_path+imit_filename) )
    h = orig.hammingDistance(imit)
    print(orig_filename + '  ' + imit_filename +'  Similarity: ' + str(round(1.0-h/128.0,2)) )

if __name__ == '__main__':
    unittest.main()

            


   