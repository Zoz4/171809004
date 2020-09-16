import sys
from tools import *
from exceptionalHandling import *

def main():
    try:
        if ( len(sys.argv) < 4 ):
            raise Error('请检查输入格式：python main.py [原文文件路径] [抄袭版论文的文件路径] [输出答案文件路径]')

        orig_filePath = sys.argv[1]
        imit_filePath = sys.argv[2]
        result_filePath = sys.argv[3]
       
        orig_text = readFile(orig_filePath)

        if(orig_text == '' ):
            raise Error("原文文件内容为空")
        if orig_text is None:
            raise Error("原文文件打开失败")

        imit_text = readFile(imit_filePath)

        if(imit_text == '' ):
            raise Error("抄袭版论文文件内容为空")
        if imit_text is None:
            raise Error("抄袭版论文文件打开失败")

        orig = SimHash( orig_text )
        imit = SimHash( imit_text )

        h = orig.hammingDistance( imit )

        writeFile( result_filePath, h )

    except Error as msg:
        print(msg)

if __name__ == '__main__':
    main()

    
