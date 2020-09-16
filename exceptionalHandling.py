
 # 自定义异常类
class Error(Exception):

    def __init__(self,content):
        self.content = content

    def __str__(self):
        return self.content



    