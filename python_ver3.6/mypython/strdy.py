# -*- coding: utf-8 -*- 

'''
Created on 2017. 6. 25.

@author: hwang-ingyu
'''
from aem.aemreference import BeginsWith
def safe_index(my_list, value):
    try :
        print(my_list.index(value))
        return my_list.index(value)
    except :
        print(None)
        return None
 
safe_index([1,2,3,4,5,6,7,8,],12)
  
list1 = [1, 2, 3, 4]
 
list1.insert(1, 8)
print(list1)
 
list1.sort()
print(list1)
 
list1.reverse()
print(list1)
  
  
shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}
try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product =='풀':
                print("{}: {}원".format(shop, price))
                raise StopIteration
except StopIteration as e:
    print(e)
     
       
class Car1():
    def run(self):
        print('{}가 달립니다.'.format(self.name))
                
class Car():

    def __init__(self, name):
        self.name = name

    def run(self):
        print("차가 달립니다.")


# class Truck(Car):
#     def __init__(self, name, capacity):
#         super(Truck, self).__init__(name)
#         self.capacity = capacity
#         print("이 자동차의 이름은 {}이고, 무개는 {}입니다.".format(name, capacity))
# 
#     def load(self):
#         print("짐을 실었습니다.")
#         
#     def run(self):
#         Car.run(self)
#         
         
taxi = Car1()
# chack = Truck("페라리!","100")
car1 = Car1()


taxi.name = "택시"
taxi.run()
# chack.__init__()


