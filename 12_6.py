import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import warnings
warnings.filterwarnings('ignore')
"""
参考
https://qiita.com/jabberwocky0139/items/e2526fc5ee3b0dbf144b
"""

##Variables
N = 20
a = 1
d = 1
kappa = 1
L = 10

def calc_ode(f,t,a,d,kappa):
    ##global a,d,kappa

    x,v = f[:N],f[N:]
    res_x = v
    x = np.append(x,[x[0]])
    diff_x = np.diff(x)
    diff_x = np.array([i if i>0 else L + i for i in diff_x])
    res_v = a*(np.tanh(kappa*(diff_x-d))+np.tanh(kappa*d)-v)
    res = np.append(res_x,res_v)

    return res

def main():

    x_init = np.arange(N)*(L/N)
    ##x_init = np.array([random.random()*2*np.pi for _ in range(N)])
    velocity_init = [0] + ([1] * (N - 1))
    init = np.append(x_init,velocity_init)
    t = np.arange(0,200,0.1)
    sol = odeint(calc_ode,init,t,args=(a,d,kappa))
    ##sol = odeint(trafficJam,init,t,args=(a,c,L),full_output=False)

    x = np.linspace(-1,1,500)
    fig = plt.figure()
    ims = []

    for i in range(480):
        tmp = plt.subplot()
        tmp.set_aspect("equal")
        upper, = plt.plot(x,np.sqrt(1-x**2),color="gray")
        lower, = plt.plot(x,-np.sqrt(1-x**2),color="gray")
        plot_x = [np.cos(2*np.pi*(j/L)) for j in sol[i][:N]]
        plot_y = [np.sin(2*np.pi*(j/L)) for j in sol[i][:N]]
        plots = plt.scatter(plot_x,plot_y,color="r",s=100)
        plt.xticks(color="None")
        plt.yticks(color="None")
        plt.tick_params(length=0)
        ims.append([upper,lower,plots])
    
    ani = animation.ArtistAnimation(fig,ims,interval=20)
    ##plt.show()
    ani.save("12_6.gif",writer="pillow")

if __name__ == "__main__":
    main()
