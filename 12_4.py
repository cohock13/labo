import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
import matplotlib.animation as animation
##subplotの警告を無視
import warnings
warnings.filterwarnings('ignore')
####パラメータ
omega = 1
dt = 0.01
x_0 = 4
rng = 30
step = int(rng/dt)

def f(phi,t,a):
    return omega - a*np.cos(phi)

def runge_kutta_method(t,a):
    runge = np.array([])
    x = x_0

    for time in t:
        runge = np.append(runge,x)
        k1 = f(x,time,a)
        k2 = f(x+0.5*k1*dt,time+0.5*dt,a)
        k3 = f(x+0.5*k2*dt,time+0.5*dt,a)
        k4 = f(x+k3*dt,time+dt,a)
        x += dt*(k1+2*k2+2*k3+k4)/6

    return runge

def plot():

    t = np.linspace(0,rng,step)
    x = np.linspace(-1,1,1000)
    fig = plt.figure()
    ims = []

    for i in range(-150,150):
        if i == 0:
            continue
        a = 0.01*i
        flag_add = False
        plt.subplot(1,2,1)
        plt.title("Solution of dφ/dt = ω - a*cos(φ)")
        plt.ylim([0,40])
        plt.xlabel("t")
        plt.ylabel("φ")
        sol, = plt.plot(t,runge_kutta_method(t,a),color="r")
        a_str = "a = "+(str(round(a,3))).ljust(5,'0')
        value_a = plt.text(15,35,a_str, horizontalalignment='center', verticalalignment='bottom',fontsize=16)

        r = plt.subplot(1,2,2)
        plt.title("Phase Plane")
        plt.xlim([-2.5,2.5])
        plt.ylim([-2.5,2.5])
        circle_upper, = plt.plot(x,np.sqrt(1-x**2),color="black")
        circle_lower, = plt.plot(x,-np.sqrt(1-x**2),color="black")
        div = omega/a
        line = r.axvline(div,ls="-.",color ="gray")
        if -1 <= div <= 1:
            flag_add = True
            unstable_point = plt.scatter([div],[np.sqrt(1-div**2)],color="red",s=30)
            stable_point = plt.scatter([div],[-np.sqrt(1-div**2)],color="black",s=30)

        if flag_add:
            ims.append([value_a,sol,circle_lower,line,circle_upper,unstable_point,stable_point])
        else:
            ims.append([value_a,sol,circle_lower,line,circle_upper])

    ani = animation.ArtistAnimation(fig, ims, interval=50)
    ##plt.show()
    ani.save("12_4.gif", writer="pillow")
    
        
if __name__ == "__main__":
    plot()
        