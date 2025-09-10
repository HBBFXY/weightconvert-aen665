[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/f6F8Yybk)
# pythonAssignment_weightConvert
### 重量转换程序。按照温度转换程序的设计思路，按照1千克=2.2046磅编写一个公制千克与英制磅的转换程序。为了方便检查代码正确性，请分别测试输入重量为10公斤和10磅的两种情况，kg和pd分别对应公斤和磅，均为小写，输入输出严格按照示例操作。输出结果保留3位小数。
### 
### 示例1：
### 10kg（为了自动评分方便，此处直接输入10kg，此括号内文字不在屏幕输出）
### 对应的英制重量为22.046磅 （此处为输出结果，此括号内文字不在屏幕输出）
### 示例2：
### 10pd （为了自动评分方便，此处直接输入10kg，此括号内文字不在屏幕输出）
### 对应的公制重量为4.535公斤 （此处为输出结果，此括号内文字不在屏幕输出）
weight=input("请输入重量并标注单位")
if weight[-2:]=='kg':
    p=eval(weight[0:-2])*2.2046
    print("转化后的重量是{:.3f}pd".format(p))
elif weight[-2:]=='pd':
    k=eval(weight[0:-2])/2.2046
    print("转化后的重量是{:.3f}kg".format(k))
else:
    print("输入错误")
