import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(-10,10,200)
X,Y = np.meshgrid(x,x)

R =np.sqrt(X**2+Y**2) 
PHI = np.arctan2(Y,X)



s = lambda r: 1/np.sqrt(np.pi)*np.exp(-r)
py = lambda r,phi: 1/(4*np.sqrt(2*np.pi))*r*np.exp(-r/2)*np.sin(phi)
px = lambda r,phi: 1/(4*np.sqrt(2*np.pi))*r*np.exp(-r/2)*np.cos(phi)

fig = plt.figure()
im = plt.imshow(py(R,PHI)**2,vmax=0.01,origin='lower',interpolation='gaussian', cmap='bone')

def animate(i):
 im.set_data(abs(np.cos(i*np.pi/800)*px(R,PHI)+np.sin(i*np.pi/800)*py(R,PHI)*np.exp(-1j*np.pi/20*i))**2)
 return im

animate = animation.FuncAnimation(fig,animate,interval=1,blit=False)

plt.show()
