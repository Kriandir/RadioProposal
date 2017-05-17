import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import Plotter as plotz

# we set radius magnetosphere as x-axis

Solarwinds = [[10e5,50e5,100e5,200e5,400e5],[10e5,50e5,100e5,200e5,400e5]]

# THIS IS NOT TRUE FOR JUPITER GOTTA FIX IT
Solarwind = abs(np.asarray(Solarwinds)-2.015e7)

# THERE IS A BETTER SOLUTION FOR THE FIGURES GOTTA FIND IT ON THE OTHER HAND 4 DIFFERENT MAGNETIC
Magnetic = [[10,20,30,40],[11,12,13,14]]
x = np.linspace(1,3,num=30)*(1.006*7.140e9)
d = [80*3.086e18,1.496e13*4.2]
sangle = 4*np.pi
epsilon = [1,1]
eta = 2e-3
Flux = []
Planets=["Wasp43b","Jupiter"]

# Make figures for multiple planets
for h in range(len(Planets)-1):
    exo = plotz.Plotfig(Planets[h])
    exo.createfig()

    # Loop over all the magnetic field strenghts,winds and Rmagneto and calculate
    for j in range(len(Magnetic[h])):
        for i in range(len(Solarwind[h])):
            Flux = []
            windspeed = "%0.1e [cm/s]" %Solarwinds[h][i]
            for g in range(len(x)):

                Flux.append(((epsilon[h]*eta*Solarwind[h][i]*(Magnetic[h][j]**2)*(x[g]**2))/(sangle*(d[h]**2)*(2.8e6*Magnetic[h][j])))/(10e-23))


            # Plot stuff
            if j >= 2:
                exo.axar[1,j-2].plot(x,Flux,label = windspeed)
                exo.axar[1,j-2].set_title("Magnetic field of "+ str(Magnetic[h][j]) + "[G]")
            else:
                exo.axar[0,j].plot(x,Flux,label = windspeed)
                exo.axar[0,j].set_title("Magnetic field of "+ str(Magnetic[h][j]) + "[G]")





plt.legend()
plt.show()
