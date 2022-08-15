# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from matplotlib import pyplot

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def change(obj):
    print(hex(id(obj)))  # 指向的是同一个对象
    obj = 10
    print(hex(id(obj)))  # 一个新对象


# 测试默认参数值
def print_info(name='未输入名字', age='未输入年龄'):
    print("输入的名字: ", name, "输入的年龄: ", age)
    return

#测试列表方法
def List_Methods():
    list_a = ['a', 'a','d', 'b','c','e']
    print(list_a)
    list_a.remove('a')
    print(list_a)
    list_a.sort()
    print(list_a)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sys.path)
    print_hi('PyCharm')
    print_info(age=23)
    print_info("马")
    print_info("牛", 23)
    List_Methods()
    temp = 3
    change(temp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
