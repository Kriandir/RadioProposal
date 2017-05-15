import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


class Plotfig:
    def __init__(self,name):
        self.name = name
        self.fig = 0
        axar = []


    def createfig(self):

        self.fig,self.axar = plt.subplots(2,2 ,sharex = 'col', sharey = 'row')
        self.axar[0,1].set_yscale('log')
        self.axar[0,1].set_ylabel("Flux [Jy]")
        self.axar[0,1].set_xlabel("Radius [cm]")
        self.axar[1,0].set_yscale('log')
        self.axar[1,0].set_ylabel("Flux [Jy]")
        self.axar[1,0].set_xlabel("Radius [cm]")
        self.fig.suptitle(self.name)
