import jieba
import jieba.analyse
import mmh3

# Read text file to a string
def readFile( file_path ):
    textStr = ''
    with open(file_path, 'r', encoding='utf8') as file_object:
        lines = file_object.readlines()
        for line in lines:
            if(line[0] != '\n'):
                textStr += line.strip()
    return textStr
 # 
def hash128ToStr( word ):
    hashcodes = mmh3.hash128(word)
    hashstr = bin(hashcodes).replace('0b','').zfill(128)
    return hashstr

class SimHash():
    def __init__(self, text):
        self.text = text
        self.simhashstr = self.simHash()

    def simHash(self):
        seg_list = jieba.lcut(self.text)
        jieba.analyse.set_stop_words('stop_words.utf8')
        words = jieba.analyse.extract_tags('|'.join(seg_list),topK=len(seg_list),withWeight=True)
        temp = []
        hashlength = 128
        for i in range(hashlength):
            temp.append(0.0)
        for feature, weight in words:
            #print("Key: "+ str(feature) + "weight: "+ str(weight))
            featureHash = (hash128ToStr(feature))
            for i in range(hashlength):
                if(featureHash[i] == '1'):
                    temp[i] += weight
                elif(featureHash[i] == '0'):
                    temp[i] -= weight
        result = ''
        #print(temp)
        for i in range(hashlength):
            if(temp[i] > 0):
                result += '1'
            else:
                result += '0'
        return result

    def hammingDistance(self, other):
        a = int(self.simhashstr, 2)
        b = int(other.simhashstr, 2)
        n = a^b
        cnt = 0
        while n:
            n &= (n-1)
            cnt += 1
        return cnt
        
def writeFile( file_path, hanmingDistance ):
    with open(file_path, 'w', encoding='utf8') as file_object:
        result = 1 - hanmingDistance/128.0
        file_object.write(str( round(result,2) ))

