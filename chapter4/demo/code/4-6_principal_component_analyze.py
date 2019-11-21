#-*- coding: utf-8 -*-
#主成分分析 降维
import pandas as pd

#参数初始化
inputfile = '../data/principal_component.xls'
outputfile = '../tmp/dimention_reducted.xls' #降维后的数据

data = pd.read_excel(inputfile, header = None) #读入数据
print(data)

from sklearn.decomposition import PCA

pca = PCA()
pca.fit(data)

pca.components_ #返回模型的各个特征向量
print(pca.components_)

pca.explained_variance_ratio_
# 返回各个成分各自的方差百分比(贡献率)
# 选取贡献率较大的成分，舍弃贡献率较小的成分
# 加和足够接近 100% 时，就认为选取的主成分可以近似代表数据的维度了
print(pca.explained_variance_ratio_)