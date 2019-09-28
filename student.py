'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/8/1 9:24
@Software: PyCharm
@File    : student.py
'''
class Student:
    def __init__(self,name,age,score):
        self.__name = name
        self.__age = age
        self.__score = score

    def get_info(self):
        return (self.__name,self.__age,self.__score)

    def get_age(self):
        return self.__age

    def get_score(self):
        return self.__score

    def write_to_file(self, f):
        f.write(self.__name)
        f.write(',')
        f.write(str(self.__age))
        f.write(',')
        f.write(str(self.__score))
        f.write('\n')
