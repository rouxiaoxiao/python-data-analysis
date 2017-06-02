#encoding=utf-8

import numpy as np


def main():
    #line
    import matplotlib.pyplot as plt
    x = np.linspace(-np.pi,np.pi,256,endpoint=True)
    c,s = np.cos(x),np.sin(x)
    plt.figure(1)
    #alpha : 透明度，值在0到1之间，0为完全透明，1为完全不透明
    plt.plot(x,c,color="blue",linewidth=1.0,linestyle="-",label="COS",alpha=0.5)
    plt.plot(x,s,"r*",label="SIN")
    plt.title("COS & SIN")
    #gca就是一个编辑器
    ax = plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data",0))
    ax.spines["bottom"].set_position(("data", 0))
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    # plt.xticks()
    plt.show()







if __name__ == '__main__':
    main()
