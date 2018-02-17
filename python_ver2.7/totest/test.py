# -*- coding: utf-8 -*- 

'''
Created on 2017. 6. 30.

@author: hwang-ingyu
'''
class A:
    def __init__(self):
        print("A 클래스의 생성자 호출!")
 
class B(A):
    def __init__(self):
        print("B 클래스의 생성자 호출!")
        super(A).__init__()
 
class C(A):
    def __init__(self):
        print("C 클래스의 생성자 호출!")
        super(A).__init__()
 
class D(B, C):
    def __init__(self):
        print("D 클래스의 생성자 호출!")
        super(B, C).__init__()

d = D()

d
