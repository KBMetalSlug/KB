import numpy as np
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

print ("1.Drop Wave\n2.Goldstein-Price\n3.Six-hump camel back")
J=int(input('Pilihan:'))

if J==1:
  X = np.arange(2,-2, -0.1)
  Y = np.arange(2,-2, -0.1)
  X, Y = np.meshgrid(X, Y)
  Z = (-1*(1 + np.cos(12*np.sqrt(X**2 + Y**2))))/((0.5*(X**2+Y**2))+2)
elif J==2:
  X = np.arange(2, -2, -0.01)
  Y = np.arange(-2, 2, 0.01)
  X, Y = np.meshgrid(X, Y)
  Z = (1 + (X + Y + 1)**2 * (19 - 14 * X + 3*X**2 - 14*Y + 6*X*Y + 3 * Y**2) * (30 + (2 * X - 3 * Y)**2 * (18 - 32 * X + 12 * X**2 + 48 * Y - 36 * X * Y + 27 * Y**2)))
elif J==3:
  X = np.arange(2, -2 , -0.01)
  Y = np.arange(1, -1, -0.01)
  X, Y = np.meshgrid(X, Y)
  Z = (4- 2.1*X**2 + X**4/3) * X**2 + X*Y + (-4 + 4*Y**2) * Y**2
else :
  print('Pilihan tidak ada')

num_func_params = 2
num_swarm = 100
position = -3 + 6 * np.random.rand(num_swarm, num_func_params)
velocity = np.zeros([num_swarm, num_func_params])
personal_best_position = np.copy(position)
personal_best_value = np.zeros(num_swarm)

for i in range(num_swarm):
    if J==1 :
        personal_best_value[i] = (-1*(1 + np.cos(12*np.sqrt(position[i][0]**2 + position[i][1]**2))))/((0.5*(position[i][0]**2+position[i][1]**2))+2)
    elif J==2 :
        personal_best_value[i] = (1 + (position[i][0] + position[i][1] + 1)**2 * (19 - 14 * position[i][0] + 3*position[i][0]**2 - 14*position[i][1] + 6*position[i][0]*position[i][1] + 3 * position[i][1]**2) * (30 + (2 * position[i][0] - 3 * position[i][1])**2 * (18 - 32 * position[i][0] + 12 * position[i][0]**2 + 48 * position[i][1] - 36 * position[i][0] * position[i][1] + 27 * position[i][1]**2)))
    elif J==3 :
        personal_best_value[i] = (4- 2.1*position[i][0]**2 + position[i][0]**4/3) * position[i][0]**2 + position[i][0]*position[i][1] + (-4 + 4*position[i][1]**2) * position[i][1]**2
    else :
        print('pilihan salah')
tmax = 200
c1 = 0.001
c2 = 0.002
levels = np.linspace(-1, 35, 100)
global_best = np.min(personal_best_value)
global_best_position = np.copy(personal_best_position[np.argmin(personal_best_value)])

for t in range(tmax):
    for i in range(num_swarm):
        if J==1 :
            error = (-1*(1 + np.cos(12*np.sqrt(position[i][0]**2 + position[i][1]**2))))/((0.5*(position[i][0]**2+position[i][1]**2))+2)
        elif J==2 :
            error = (1 + (position[i][0] + position[i][1] + 1)**2 * (19 - 14 * position[i][0] + 3*position[i][0]**2 - 14*position[i][1] + 6*position[i][0]*position[i][1] + 3 * position[i][1]**2) * (30 + (2 * position[i][0] - 3 * position[i][1])**2 * (18 - 32 * position[i][0] + 12 * position[i][0]**2 + 48 * position[i][1] - 36 * position[i][0] * position[i][1] + 27 * position[i][1]**2)))
        elif J==3 :
            error = (4- 2.1*position[i][0]**2 + position[i][0]**4/3) * position[i][0]**2 + position[i][0]*position[i][1] + (-4 + 4*position[i][1]**2) * position[i][1]**2
        else :
            print('pilihan salah')
        if personal_best_value[i] > error:
            personal_best_value[i] = error
            personal_best_position[i] = position[i]
    best = np.min(personal_best_value)
    best_index = np.argmin(personal_best_value)
    if global_best > best:
        global_best = best
        global_best_position = np.copy(personal_best_position[best_index])

    for i in range(num_swarm):
        #update velocity
        velocity[i] += c1 * np.random.rand() * (personal_best_position[i]-position[i]) \
                    +  c2 * np.random.rand() * (global_best_position - position[i])
        position[i] += velocity[i]

    fig = plt.figure()
    CS = plt.contour(X, Y, Z, levels =levels, cmap=cm.gist_stern)
    plt.gca().set_xlim([-3,3])
    plt.gca().set_ylim([-3,3])
    for i in range(num_swarm):
        plt.plot(position[i][0], position[i][1], 'go')
    plt.plot(global_best_position[0], global_best_position[1], 'ro')

    plt.title('{0:03d}'.format(t))
    filename = 'img{0:03d}.png'.format(t)
    plt.savefig(filename, bbox_inches='tight')
    plt.close(fig)