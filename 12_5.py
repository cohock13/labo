import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
import matplotlib.animation as animation

##subplotの警告を無視
import warnings
warnings.filterwarnings('ignore')
####パラメータ
omega = 1
rng = 500
step = 10000
eps = 0.05

def calc_ode(var,t,omega,eps):
    return [omega-eps*np.sin(var[0]-var[1]),omega-eps*np.sin(var[1]-var[0])]


def plot():

    t = np.linspace(0,rng,step)
    sol = odeint(calc_ode,[3,7],t,args=(omega,eps))
    sol_2 = odeint(calc_ode,[3,4],t,args=(omega,eps))

    plt.title("φ_2 - φ_1")
    plt.plot(t,sol[:,1]-sol[:,0],label="φ_2 = 7 , φ_1 = 3")
    plt.plot(t,sol_2[:,1]-sol_2[:,0],label="φ_2 = 4 , φ_1 = 3")
    plt.legend()
    
    plt.show()
    
        
if __name__ == "__main__":
    plot()
        