'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/7/28 14:17
@Software: PyCharm
@File    : main.py
'''
from day16.menu import show_menu
# from day16.student_info import *
import day16.student_info as si

def main():
    while True:
        show_menu()
        s = input("请选择:")
        if s == 'q':
            return
        if s == '1':
            si.add_student()
        elif s == '2':
            si.list_all_student()
        elif s == '3':
            name = input("请输入学生姓名：")
            docs = si.remove_student(name,docs)
        elif s == '4':
            name = input("请输入学生姓名：")
            if not name:
                continue
            age = int(input("请输入学生年龄："))
            score = int(input("请输入学生成绩："))
            docs = si.update_student(name,age,score)
        elif s == '5':
            si.list_order_by_score_desc()
        elif s == '6':
            si.list_order_by_score_asc()
        elif s == '7':
            si.list_order_by_age_desc()
        elif s == '8':
            si.list_order_by_age_asc()
        elif s == '9':
            si.save_to_file()
        elif s == '10':
            filename = 'six.txt'
            si.read_from_file(filename)

if __name__ == '__main__':#判断当前模块是不是主模块
    main()
