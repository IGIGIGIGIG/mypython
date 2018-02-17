# -*- coding: utf-8 -*-
'''
Created on 2017. 6. 24.

@author: hwang-ingyu
'''
from Crypto.Random.random import choice
from _curses import version
from boto import Version

class hello(object):
    def __init__(self):
        self.name = "whang"
    
ho = hello()
print(ho.name)

class hi(hello):
    def __init__(self):
        self.name = "ingyu"
        
to_hi = hi()
        
print(to_hi.name)

class to_hell_with_the_deliv:
    def __init__(self):
        self.name = """we speck of the deliv
        to the frinder minde
        trun for give me we went we to hell go
        
        to hell with the deliv
        to hell with the deliv
        to hell with the deliv"""
        
kasa = to_hell_with_the_deliv()

class lalabel():
    def __init__(self):
        list = [1,2,3,4,5,6,7,8,9]
        self.list1 = choice(list)

lalabel = lalabel()

print(kasa.name)
print(lalabel.list1)


class layvel(lalabel):
    '''extends lalabel'''
    def __init__(self):
        if list in list< 10 :
            print("정상적으로 상속 받았어요~~")
        
        else:
            print("미안하지만 난 제대로 상속받지 못했어")
        
class inote():
    def __init__(self):
        pylist = ["list1","list2", "list3", "list4", "list5"]
        print(pylist)
        
hisname = inote()

print(hisname.__init__())
        
        
        
        
        
        
        
        
        
        
        
        
        