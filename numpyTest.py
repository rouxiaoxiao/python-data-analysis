#encoding=utf-8

#使用较多的库用简化形式较为简单
import numpy as np


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




















if __name__ == '__main__':
    main()
