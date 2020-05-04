import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint

####parameters
dt = 0.01
rng = 40
step = int(rng/dt)
x_0 = 0.0
tau_list = [0.1,3,20]
a = 2

def f(x,t,tau):
    return (a*np.sin(t)-x)/tau

def runge_kutta_method(t,tau):
    runge = np.array([])
    x = x_0

    for time in t:
        runge = np.append(runge,x)
        k1 = f(x,time,tau=tau)
        k2 = f(x+0.5*k1*dt,time+0.5*dt,tau=tau)
        k3 = f(x+0.5*k2*dt,time+0.5*dt,tau=tau)
        k4 = f(x+k3*dt,time+dt,tau=tau)
        x += dt*(k1+2*k2+2*k3+k4)/6

    return runge

def plot():

    t = np.linspace(0,rng,step)

    plt.title("solution of dx/dt = (asin(t)-x)/τ")
    plt.xlabel("t")
    plt.ylabel("f")
    
    for tau in tau_list:
        plt.plot(t,runge_kutta_method(t,tau),label="tau:"+str(tau))
    
    plt.plot(t,np.sin(t),label="asin(t)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot()
        