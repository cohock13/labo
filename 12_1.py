##ライブラリのインポート
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint

####パラメータ
tau = 3
a = 2
dt = 0.2
rng = 20
step = int(rng/dt)+1
x_0 = 0.0

##fを返す
def f(x,t):
    return (a-x)/tau

##ルンゲクッタ法の計算
def runge_kutta_method(t):
    runge = np.array([])
    x = x_0

    for time in t:
        runge = np.append(runge,x)
        k1 = f(x,time)
        k2 = f(x+0.5*k1*dt,time+0.5*dt)
        k3 = f(x+0.5*k2*dt,time+0.5*dt)
        k4 = f(x+k3*dt,time+dt)
        x += dt*(k1+2*k2+2*k3+k4)/6

    return runge


##オイラー法の計算
def euler_method(t):
    e = np.array([])
    x = x_0
    for time in t:
        e = np.append(e,x)
        x += dt*f(x,time)
    return e

##PythonライブラリのScipyの常微分方程式のソルバ
def scipy_ode_solver(t):
    s = np.array([])
    for i in odeint(f,x_0,t):
        s = np.append(s,i[0])
    return s

##厳密解
def exact_solution(t):
    return (x_0-a)*np.exp(-t/tau) + a


##プロットをする.Matplotlibというライブラリを使う.
def plot():

    t = np.linspace(0,rng,step)

    exact = exact_solution(t)
    rungekutta = runge_kutta_method(t)
    euler = euler_method(t)
    solver = scipy_ode_solver(t)
    
    """
    ###プロット部分
    plt.title("solution of dx/dt = (a-x)/τ")
    plt.xlabel("t")
    plt.ylabel("f")
    plt.plot(t,rungekutta,label="runge-kutta-method")
    plt.plot(t,euler,label="euler-method")
    plt.plot(t,solver,label="scipy-odeint")

    """
    ##誤差計算(コメントアウト)
    plt.title("error of solutions")
    plt.xlabel("t")
    plt.ylabel("f")
    plt.plot(t,np.log10(abs(rungekutta-exact)),label="runge-kutta-method")
    plt.plot(t,np.log10(abs(euler-exact)),label="euler-method")
    plt.plot(t,np.log10(abs(solver-exact)),label="scipy-odeint")
    

    plt.legend()
    plt.show()


##main関数として呼ばれたときに実行
if __name__ == "__main__":
    plot()
        