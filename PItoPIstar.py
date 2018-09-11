import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(-10,10,200)
X,Y = np.meshgrid(x,x)

d = 2
R1 =np.sqrt((X-d)**2+Y**2)
R2 = np.sqrt((X+d)**2+Y**2)
PHI1 = np.arctan2(Y,(X-d))
PHI2 = np.arctan2(Y,(X+d))



s = lambda r: 1/np.sqrt(np.pi)*np.exp(-r)
py = lambda r,phi: 1/(4*np.sqrt(2*np.pi))*r*np.exp(-r/2)*np.sin(phi)
px = lambda r,phi: 1/(4*np.sqrt(2*np.pi))*r*np.exp(-r/2)*np.cos(phi)

PI = 1/np.sqrt(2)*(py(R1,PHI1) + py(R2,PHI2))
PIstar = 1/np.sqrt(2)*(py(R1,PHI1) - py(R2,PHI2))

fig = plt.figure()
im = plt.imshow(PI**2,vmax=0.005,origin='lower',interpolation='gaussian', cmap='bone')

def animate(i):
 im.set_data(abs(np.cos(i*np.pi/1000)*PI+np.sin(i*np.pi/1000)*PIstar*np.exp(-1j*np.pi/20*i))**2)
 return im

animate = animation.FuncAnimation(fig,animate,interval=1,blit=False)

plt.show()
