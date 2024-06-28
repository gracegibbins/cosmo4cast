import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt

gal_z0 = np.zeros(3072)
gal_z1 = np.zeros(3072)
gal_z2 = np.zeros(3072)
gal_z3 = np.zeros(3072)
gal_z4 = np.zeros(3072)

#Sepereates data into approp gal_z wrt z-bins with gal_z objs being 2000x3072 where rows are relizations and columns are ps values at same l value
for m in range(2000): #iterates through maps
    gal = np.load('noiseps/clgg_allz_'+str(m)+'.npy')
    z0, z1, z2, z3, z4 = gal
    gal_z0 = np.vstack((gal_z0, z0))
    gal_z1 = np.vstack((gal_z1, z1))
    gal_z2 = np.vstack((gal_z2, z2))
    gal_z3 = np.vstack((gal_z3, z3))
    gal_z4 = np.vstack((gal_z4, z4))

#removes first row of zeros
gal_z0 = np.delete(gal_z0, 0, axis = 0)
gal_z1 = np.delete(gal_z1, 0, axis = 0)
gal_z2 = np.delete(gal_z2, 0, axis = 0)
gal_z3 = np.delete(gal_z3, 0, axis = 0)
gal_z4 = np.delete(gal_z4, 0, axis = 0)

mean_z0 = []
mean_z1 = []
mean_z2 = []
mean_z3 = []
mean_z4 = []

for l in range(3072):
    mean_z0.append(np.mean(gal_z0[:,l]))
    mean_z1.append(np.mean(gal_z1[:,l]))
    mean_z2.append(np.mean(gal_z2[:,l]))
    mean_z3.append(np.mean(gal_z3[:,l]))
    mean_z4.append(np.mean(gal_z4[:,l]))

x = np.arange(0,3072)

plt.plot(x, mean_z0)
plt.show()


'''
For checksies:
meanz00 = (gal_z0[0,0] + gal_z0[1,0]) /2

print(mean_z0[0],meanz00 )
'''











#    wl = np.load('noiseps/clkkgal_allz_'+str(m)+'.npy')
'''
Iterates over the 3072 values for each power spectra, finding the mean of each value. This is appended to a list.


for p in range(2000): #p is a single power spectrum
    ps = gal_z0[p]
    for v in range(3072): #iterestes through 2d list of power spectra list -> p is amp of ps for each realization
        sum += ps[v]

#    av = np.mean(ps[v], )
#    gal_z0_av.append(av)

    
for m in range(2000): #iterates through maps
    gal = np.load('noiseps/clgg_allz_'+str(m)+'.npy')
    gal_all.append

g0 = np.empty((1,3072))
g1 = np.empty((1,3072))
g2 = np.empty((1,3072))
g3 = np.empty((1,3072))
g4 = np.empty((1,3072))

for m in range(2000): #iterates through maps
    gal = np.load('noiseps/clgg_allz_'+str(m)+'.npy')
    for z in range(5):
        if z == 0:
            for maps in range(
            np.insert(g0, [m], gal[0,:])
'''
