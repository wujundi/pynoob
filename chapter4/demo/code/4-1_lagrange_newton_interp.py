#拉格朗日插值代码
import pandas as pd #导入数据分析库Pandas
from scipy.interpolate import lagrange #导入拉格朗日插值函数

inputfile = '../data/catering_sale.xls' #销量数据路径
outputfile = '../tmp/sales.xls' #输出数据路径

data = pd.read_excel(inputfile) #读入数据
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None #过滤异常值，将其变为空值
print(data)

#自定义列向量插值函数
#s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
def ployinterp_column(s, n, k=5):
  y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))] #取数
  y = y[y.notnull()] #剔除空值
  return lagrange(y.index, list(y))(n) #插值并返回插值结果

#逐个元素判断是否需要插值
for i in data.columns: # 最外层循环是列，也就是说本程序的思路是先处理第一列，再处理第二列，就白白扫过了第一列
  for j in range(len(data)):
    # print(data[i][j])
    if (data[i].isnull())[j]: #如果为空即插值。
      # data[i].isnull() 会以一个列向量的形式返回 data[i] 这一列的各行是否是 null (True/False)
      # 在 data[i].isnull() 返回结果中的【第j个】就是第j个元素是否为 null 的结果了
      # 所以 (data[i].isnull())[j] 可以理解成 1、data[i].isnull() -> Array  2、Array[j] = true
      data[i][j] = ployinterp_column(data[i], j)

data.to_excel(outputfile) #输出结果，写入文件
