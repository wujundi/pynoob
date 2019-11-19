# -*- coding: utf-8 -*-
import pandas as pd #通常用pd作为pandas的别名。

s = pd.Series([1,2,3], index=['a', 'b', 'c']) #创建一个序列s 序列是KV对的集合
d = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns = ['a', 'b', 'c']) #创建一个表，DataFRame是表的形式
d2 = pd.DataFrame(s) #也可以用已有的序列来创建表格

print(d)
d.head() #预览前5行数据
print(d.head())
d.describe() #数据基本统计量
print(d.describe())

print(d2)
d2.head() #预览前5行数据
print(d2.head())
d2.describe() #数据基本统计量
print(d2.describe())

#读取文件，注意文件的存储路径不能带有中文，否则读取可能出错。
# pd.read_excel('data.xls') #读取Excel文件，创建DataFrame。
# pd.read_csv('data.csv', encoding = 'utf-8') #读取文本格式的数据，一般用encoding指定编码。
