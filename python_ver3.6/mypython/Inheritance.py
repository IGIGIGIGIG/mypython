# -*- coding: utf-8 -*- 

'''
Created on 2017. 6. 29.

@author: hwang-ingyu
'''

# class peple1:
#     def __init__(self):
#         print("class peple1이 호출되었습니다.")
#          
# class peple2(peple1):
#     def __init__(self):
#         print("class peple2가 호출되었습니다.")
#         super().__init__()
#  
# class peple3(peple1):
#     def __init__(self):
#         print("class peple3이 호출되었습니다.")
#         super().__init__()
#      
# class peple4(peple2, peple3):
#     def __init__(self):
#         print("class peple4가 호출되었습니다.")
#         super().__init__()
#          
# hello = peple4()
#  
# hello


class person:
    def __init__(self, str):
        self.str = str
    def method(self):
        print("{}가 ".format(str))
        
class hi(person):
    def __init__(self, str):
        super().__init__(str)
    
    def method(self):
        super().method()
        print("인사합니다.")


iii = hi("인규가")
iii.__init__()


