import jieba
import jieba.analyse
import mmh3
from exceptionalHandling import *

# 读入文件，去掉多余空白后转为字符串返回
def readFile( file_path ):

    textStr = ''
    try:
        with open(file_path, 'r', encoding='utf8') as file_object:
            lines = file_object.readlines()
            for line in lines:
                if(line[0] != '\n'):
                    textStr += line.strip()
        return textStr
    except FileNotFoundError:
        msg = '路径：'+ file_path + ' 中未找到文件'
        print(msg)
        return None

 # 词语用普通hash函数散列，hash采用的是murmurhash3
 # 将得到的128位长的int类型数转换为二进制“0-1”字符串返回

def hash128ToStr( word ):
    hashcodes = mmh3.hash128(word)
    hashstr = bin(hashcodes).replace('0b','').zfill(128)
    return hashstr

class SimHash():
    def __init__(self, text = ''):
        self.text = text
        self.simhashstr = self.simHash()

 # 计算128位长的Simhash值
    def simHash(self):
        # 用jieba分词对文本进行分词
        seg_list = jieba.lcut(self.text)
            # 设置停用词，并用TF-IDF模型计算词的权重
        jieba.analyse.set_stop_words('stop_words.utf8')
        words = jieba.analyse.extract_tags('|'.join(seg_list),topK=len(seg_list),withWeight=True)

        if(len(words)==0):
            raise Error('字典中没有词语')

        temp = []
        hashlength = 128
        # 初始化一个含有 128个0 的空列表，用于统计加权后的值
        for i in range(hashlength):
            temp.append(0.0)
        for feature, weight in words:
            featureHash = hash128ToStr(feature)
            for i in range(hashlength):
                if(featureHash[i] == '1'):
                    temp[i] += weight
                elif(featureHash[i] == '0'):
                    temp[i] -= weight

        # 用result储存降维后的值，即Simhash值
        result = ''
        for i in range(hashlength):
            if(temp[i] > 0):
                result += '1'
            else:
                result += '0'
        return result
 # 计算海明距离，将以二进制“0-1”字符串储存的Simhash值转为int型数值
 # 增加计算速度
    def hammingDistance(self, other):
        a = int(self.simhashstr, 2)
        b = int(other.simhashstr, 2)
        n = a^b
        cnt = 0
        while n:
            n &= (n-1)
            cnt += 1
        return cnt

 # 将结果写入目的文件
def writeFile( file_path, hanmingDistance ):
    try:
        with open(file_path, 'w', encoding='utf8') as file_object:
            result = 1.0 - hanmingDistance/128.0
            file_object.write(str( round(result,2) ))
    except FileNotFoundError:
        msg = '输出路径：'+ file_path + ' 错误'+'\n结果写入失败 '
        print(msg)

