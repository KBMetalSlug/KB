import numpy as np
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
from random import randint
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

tmax = 181
c1 = 0.001
c2 = 0.002

#burung
paramburung = 2
burung = 15
position = np.zeros([burung, paramburung])
for i in range(burung):
    position[i][0] = random.uniform(-3, 0)
    position[i][1] = random.uniform(-3, 0)
velocity = np.zeros([burung, paramburung])

jarak = []
prev = []
dx = []
dy = []
for i in range(burung):
    jarak.append(0)
    prev.append(0)
    dx.append(0)
    dy.append(0)

sekon = 15

for i in range(burung):
    jarak[i] = 50
    prev[i] = 0
    dx[i] = 0
    dy[i] = 0

for t in range (tmax):
    for i in range (burung):
        perpindahanx = np.random.rand()
        perpindahany = np.random.rand()
        tempx = perpindahanx / sekon
        tempy = perpindahany / sekon
        velocity[i][0] = tempx
        velocity[i][1] = tempy
        if position[i][0] + velocity[i][0] < 6 :
            dx[i] = 0
        else :
            dx[i] = 1
        if position[i][1] + velocity[i][1] < 6  :
            dy[i] = 0
        else :
            dy[i] = 1
        if dx[i]==0 :
            position[i][0] += velocity[i][0]
        else :
            position[i][0] -= velocity[i][0]
        if dy[i]==0 :
            position[i][1] += velocity[i][1]
        else :
            position[i][1] -= velocity[i][1]

    print (position[i])

    fig = plt.figure()
    plt.gca().set_xlim([-3, 6])
    plt.gca().set_ylim([-3, 6])

    for i in range(burung):
        plt.plot(position[i][0], position[i][1], 'go')

    plt.title('{0:03d}'.format(t))
    filename = 'img{0:03d}.png'.format(t)
    plt.savefig(filename, bbox_inches='tight')
    plt.close(fig)
