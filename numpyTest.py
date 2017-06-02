#encoding=utf-8

#使用较多的库用简化形式较为简单
import numpy as np
from numpy.linalg import *

def main():


    #Chapter 1
    #ndarray

    lst = [[1,3,5],[2,4,6]]
    # 显示对象类型
    print(type(lst))
    # list中既可以放数字也可以放字符

    np_lst = np.array(lst)
    print(type(np_lst))


    #定义数据类型必须带numpy前缀  np
    #np.array中的数据类型有bool,int,int8,int16,int32,int64,int128,uint8,uint16,uint32,uint64,uint128(无符号),float16/32/64,complex64/128
    np_lst = np.array(lst,dtype=np.float)
    print(np_lst.shape)

    # 维数
    print(np_lst.ndim)

    #数据类型
    print(np_lst.dtype)

    #每个元素的大小，因为数据类型是float64,64位占8个字节
    print(np_lst.itemsize)

    #大小，其中一共有6个元素，一共有6*8个字节
    print(np_lst.size)

    #chapter 2
    #Some Arrays  一些常用数组


    #数值初始化
    print(np.zeros([2,4]))
    print(np.ones([3,5]))
    print("Rand:")
    print(np.random.rand(2,4))
    print(np.random.rand())
    print("RandInt:")
    print(np.random.randint(1,10,3))
    #标准正态分布的随机数
    print("Randn:")
    print(np.random.randn(2,4))
    print("Choice:")
    print(np.random.choice([10,20,30]))

    print("Distribute:")
    #1到10生成100个beta分布，random中还有用二项分布等常用分布
    print(np.random.beta(1,10,100))

    #numpy的操作

    #产生等差数列，包括1，不包括11
    print(np.arange(1,11))
    print(np.arange(1, 11).reshape([2,5]))
    print(np.arange(1, 11).reshape([2, -1]))#5可以缺省为-1
    lst = np.arange(1,11).reshape([2,-1])
    #自然指数
    print(np.exp(lst))
    #2的对应次方
    print(np.exp2(lst))
    print("Sqrt:")
    print(np.sqrt(lst))
    print(np.sin(lst))
    print(np.log(lst))#底数是自然底数

    lst = np.array([[[1,2,3,4],
                     [4,5,6,7]],
                    [[7,8,9,10],
                     [10,11,12,13]],
                    [[14,15,16,17],
                     [18,19,20,21]]
                    ])
    print(lst.sum())
    print(lst.sum(axis=0))
    print(lst.sum(axis=1))
    print(lst.sum(axis=2))
    # print(lst.sum(axis=3))会报错 axis是其深入的程度
    print(lst.max())
    print(lst.max(axis=1))
    print(lst.min(axis=0))

    lst1 = np.array([10,20,30,40])
    lst2 = np.array([4,3,2,1])
    print("add:")
    print(lst1+lst2)
    print("sub:")
    print(lst1-lst2)
    print("mul:")
    print(lst1*lst2)
    print("div:")
    print(lst1/lst2)
    print("square:")
    print(lst1**2)#求平方
    #矩阵相乘
    print("dot:")
    print(np.dot(lst1.reshape([2,2]),lst2.reshape([2,2])))
    #数组追加
    print("Concatenate:")
    print(np.concatenate((lst1,lst2),axis=0))
    print(np.vstack((lst1,lst2)))
    print(np.hstack((lst1,lst2)))
    print(np.split(lst1, 2))
    print(np.split(lst1, 4))
    print(np.copy(lst1))


    #Chapter 4 liner algebra

    #生成3阶单位矩阵
    print(np.eye(3))
    lst = np.array([[1,2],
                    [3,4]])
    #逆矩阵
    print("Inv:")
    print(inv(lst))

    print("T:")
    print(lst.transpose())

    #行列式
    print("Det:")
    print(det(lst))
    #特征值和特征向量，第一个array是表示特征值，第二个array表示特征向量
    print(eig(lst))
    #解方程组，x+2y=5，3x+4y=7
    y = np.array([[5.],[7.]])
    print("Solve")
    print(solve(lst,y))

    #Chapter 5 Others
    #信号处理中的变换
    print("FFT:")
    #fft模块的fft操作
    print(np.fft.fft(np.array([1,1,1,1,1,1,1,1])))
    #对于常数的fft操作得到的就是一个阶跃


    #相关系数，皮尔逊相关系数ρxy  协方差和标准差的商
    #因为其可以计算多个数据集的相关系数，所以返回矩阵，其中-0.886就是这两个数据集的相关系数，自相关系数为1
    print("Coef:")
    print(np.corrcoef([1,0,1],[0,2,1]))

    #多项式函数
    print("Poly:")
    p = np.poly1d([1,5,6])
    print(np.roots(p))

























if __name__ == '__main__':
    main()
