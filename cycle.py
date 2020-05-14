import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
import matplotlib.animation as animation
import random
##subplotの警告を無視
import warnings
warnings.filterwarnings('ignore')
####パラメータ
omega = 1
rng = 20
step = 600
eps = 2
N = 8

def q(x,y):
    ##return np.sin(x-y)
    return np.cos(x-y)

def calc_ode(var,t,omega,eps):
    tmp = []
    for i in range(N):
        order_param = 0
        for j in range(N):
            if i != j:
                order_param += q(var[i],var[j])
        tmp.append(omega-order_param*eps)
    
    return tmp

def plot():

    t = np.linspace(0,10,500)
    phase_init = [2*np.pi*i/N for i in range(N)]
    phase_init[1] = phase_init[0] + 0.4
    sol = odeint(calc_ode,phase_init,t,args=(omega,eps))

    fig = plt.figure()
    ims = []
    x = np.linspace(-1,1,500)

    for i in range(500):
        tmp = plt.subplot()
        tmp.set_aspect("equal")
        plots_x = [np.cos(sol[i][j]) for j in range(N)]
        plots_y = [np.sin(sol[i][j]) for j in range(N)]
        upper, = plt.plot(x,np.sqrt(1-x**2),color="gray")
        lower, = plt.plot(x,-np.sqrt(1-x**2),color="gray")
        plots = plt.scatter(plots_x,plots_y,color="r",s=100)
        plt.xticks(color="None")
        plt.yticks(color="None")
        plt.tick_params(length=0)
        ims.append([plots,upper,lower])
    
    ani = animation.ArtistAnimation(fig,ims,interval=20)
    ##plt.show()
    ani.save("cycle.gif",writer="pillow")
    
        
if __name__ == "__main__":
    plot()