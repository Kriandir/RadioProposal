import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# we set radius magnetosphere as x-axis

Solarwinds = [10e5,50e5,100e5,200e5,400e5]
Solarwind = abs(np.asarray(Solarwinds)-2.015e7)

Magnetic = [10,20,30,40]
x = np.linspace(1,3,num=30)*(1.006*7.140e9)
d = 80*3.086e18
angle = 4*np.pi
Flux = []

for j in range(len(Magnetic)):
    for i in range(len(Solarwind)):
        Flux = []
        windspeed = "%0.1e [cm/s]" %Solarwinds[i]
        for g in range(len(x)):

            Flux.append(((Solarwind[i]*(Magnetic[j]**2)*(x[g]**2))/(angle*(d**2)*(2.8e6*Magnetic[j])))/(10e-23))
        plt.plot(x,Flux,label = windspeed)
    plt.yscale('log')
    plt.ylabel("Flux [Jy]")
    plt.xlabel("Radius [cm]")
    plt.title("Magnetic field of " + str(Magnetic[j])+"[G]")
    plt.legend()
    plt.show()
