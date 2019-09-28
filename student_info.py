'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/7/28 14:17
@Software: PyCharm
@File    : make.py
'''
from day16.student import Student
docs = []#此列表用来存储所有学生信息

def input_student():
    students = []
    while True:
        name = input("请输入学生姓名：")
        if not name:
            break
        age = int(input("请输入学生年龄："))
        score = int(input("请输入学生成绩："))
        student = Student(name,age,score)
        # student = {'name': name,'age':age,'score':score}
        students.append(student)
    return students

def add_student():
    """添加学生的函数供其他模块使用"""
    global docs
    docs += input_student()


def output_student(lst):
    print("+-----------+--------+---------+")
    print("|   name    |  age   |  score  |")
    print("+-----------+--------+---------+")
    for student in lst:
        info = "|%11s|%8d|%9d|"%student.get_info()
        print(info)
    print("+-----------+--------+---------+")

def list_all_student():
    """列表所有学生信息的函数供其他模块使用"""
    output_student(docs)

def remove_student(name,lst):
    lst1 = []
    for i in lst:
        if name not in i['name'] :
            lst1.append(i)
            print(name," 已删除")
    return lst1

def update_student(name,age,score,lst):
    lst1 = []
    student = {'name': name, 'age': age, 'score': score}
    for i in lst:
        if name in i['name']:
            i.update(student)
            print(name, "已修改")
        lst1.append(i)
    return lst1

def list_order_by_score_desc():
    L = sorted(docs,key=lambda stu:stu.get_score(),reverse=True)
    output_student(L)

def list_order_by_score_asc():
    L = sorted(docs, key=lambda stu: stu.get_score())
    output_student(L)

def list_order_by_age_desc():
    L = sorted(docs,key=lambda stu:stu.get_age(),reverse=True)
    output_student(L)

def list_order_by_age_asc():
    L = sorted(docs, key=lambda stu: stu.get_age())
    output_student(L)

def save_to_file():
    try:
        file = open('si.txt','w')
        for student in docs:
            student.write_to_file(file)
        file.close()
    except IOError:
        print("保存失败")



def read_from_file():
    file = open('si.txt','r')
    for i in file.readlines():
        print(i)
    file.close()