import pandas as pd  
import numpy as np
import queue as que
import random
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import cm as CM
from matplotlib import mlab as ML

import os

df=pd.read_csv('profit1000.txt', header=0)

matrix100_= df[(df['Perbet'] == 100)]['Money'] 
matrix_round100_= df[(df['Perbet'] == 100)]['Round']
matrix200_= df[(df['Perbet'] == 200)]['Money'] 
matrix_round200_= df[(df['Perbet'] == 200)]['Round']
matrix300_= df[(df['Perbet'] == 300)]['Money'] 
matrix_round300_= df[(df['Perbet'] == 300)]['Round']
                    
matrix500_= df[(df['Perbet'] == 500)]['Money'] 
matrix_round500_= df[(df['Perbet'] == 500)]['Round']
matrix400_= df[(df['Perbet'] == 400)]['Money'] 
matrix_round400_= df[(df['Perbet'] == 400)]['Round']

def plot_models(x, y, models, fname, mx=None, ymax=None, xmin=None):
    plt.clf()
    plt.scatter(x, y, s=10)
    plt.title(fname)
    plt.xlabel("round")
    plt.ylabel("money")
    

    if models:
        if mx is None:
            mx = sp.linspace(0, x[-1], 1000)
        for model, style, color in zip(models, linestyles, colors):
            # print "Model:",model
            # print "Coeffs:",model.coeffs
            plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)

        plt.legend(["d=%i" % m.order for m in models], loc="upper left")

    plt.autoscale(tight=True)
    plt.ylim(ymin=0)
    if ymax:
        plt.ylim(ymax=ymax)
    if xmin:
        plt.xlim(xmin=xmin)
    plt.grid(True, linestyle='-', color='0.75')
    plt.savefig(fname)
def plot_modelh(x, y, models, fname, mx=None, ymax=None, xmin=None):
    plt.clf()
    plt.scatter(x, y, s=10)
    plt.title(fname)
    plt.xlabel("round")
    plt.ylabel("money")
    

    hist, xedges, yedges = np.histogram2d(x,y)
    X,Y = np.meshgrid(xedges,yedges)
    plt.imshow(hist)
    plt.grid(True)
    plt.colorbar()  
    plt.savefig(fname)
plot_modelh(matrix_round100_,matrix100_, None,  "100.png")
                              
plot_modelh(matrix_round500_,matrix500_, None,  "500.png")

plot_modelh(matrix_round200_,matrix200_, None,  "200.png")
plot_modelh(matrix_round300_,matrix300_, None,  "300.png")
plot_modelh(matrix_round400_,matrix400_, None,  "400.png")

