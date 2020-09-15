import jieba
import jieba.analyse
import mmh3

# Read text file to a string
def readFile( File_path ):
    textStr = ''
    with open(File_path, 'r', encoding='utf8') as file_object:
        lines = file_object.readlines()
        for line in lines:
            textStr += line.strip()
    return textStr

def hash64ToStr( word ):
    hashcodes = mmh3.hash64(word, signed = False)
    hashstr = bin(hashcodes[0]).replace('0b','').zfill(64)
    return hashstr

class SimHash():
    def __init__(self, text):
        self.text = text
        self.simhashstr = self.simHash()

    def simHash(self):
        #print(self.text)
        jieba.analyse.set_stop_words('stop_words.utf8')
        seg_list = jieba.lcut(self.text)
        #print('|'.join(seg_list))
        words = jieba.analyse.extract_tags('|'.join(seg_list),topK=32,withWeight=True)
        temp = []
        length = 64
        for i in range(length):
            temp.append(0.0)

        for feature, weight in words:
            print("Key: "+ str(feature) + "weight: "+ str(weight))
            featureHash = (hash64ToStr(feature))
            for i in range(length):
                if(featureHash[i] == '1'):
                    temp[i] += weight
                elif(featureHash[i] == '0'):
                    temp[i] -= weight
        result = ''
        for i in range(length):
            if(temp[i] > 0):
                result += '1'
            else:
                result += '0'
        return result

    def hanmingDistance(self, other):
        a = int(self.simhashstr, 2)
        b = int(other.simhashstr, 2)
        n = a^b
        cnt = 0
        while n:
            n &= (n-1)
            cnt += 1
        return cnt
        
def Test():
    origFile_path = 'C:\\Users\\2024\\Desktop\\sim_0.8\\orig.txt'
    testFile_path = 'C:\\Users\\2024\\Desktop\\sim_0.8\\'
    orig = SimHash(readFile(origFile_path))
    fileNames = ['orig.txt',
            'orig_0.8_add.txt','orig_0.8_del.txt',
           'orig_0.8_dis_3.txt','orig_0.8_dis_7.txt',
            'orig_0.8_dis_10.txt','orig_0.8_dis_15.txt',
            'orig_0.8_mix.txt','orig_0.8_rep.txt','other.txt']
    for fileName in fileNames:
        test = SimHash(readFile(testFile_path+fileName))
        hanmingDistant = orig.hanmingDistance(test)
        print( fileName +' 汉明距离：'+ str(hanmingDistant) + ' 相似度: '+ 
              str(1.0-hanmingDistant/64.0) )

Test()
