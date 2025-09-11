# 在这个文件下编写代码，题目具体要求见README.md文件
weight=input()
if weight[-2:] in ['kg']:
    p=eval(weight[0:-2])*2.2046
    print("对应的英制重量为{:.3f}磅".format(p))
elif weight[-2:] in ['pd']:
    k=eval(weight[0:-2])/2.2046
    print("对应的公制重量为{:.3f}公斤".format(k))
else:
    print("输入错误")
