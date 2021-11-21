import matplotlib.pyplot as plt
from sympy import symbols, Function, Eq, dsolve, sqrt
from scipy.integrate import odeint
import numpy as np

scale = 1000  # сколько точек в диапазоне [0, 10] брать

"""решение с помощью sympy"""
x = symbols('x')
y = symbols('y', cls=Function)

eq = Eq(y(x).diff(x), -2 * y(x))
res = dsolve(eq, y(x), ics={y(0): sqrt(2)})
x_arr = np.linspace(0, 10, scale)

# следующая строчка заняла больше времени на свое написание, чем вся остальная лаба
res_sym = [float(str([res.evalf(subs={x: i})][-1]).split()[-1][:-1]) for i in x_arr]

plt.plot(x_arr, res_sym, label='simpy')

"""решение с помощью scipy"""
plt.plot(x_arr, odeint(lambda y, x: -2 * y, np.sqrt(2), x_arr), label='scipy')

plt.legend()
plt.savefig("ep3_result.png")

plt.clf()
plt.plot(x_arr, np.abs(res_sym - np.transpose(odeint(lambda y, x: -2 * y, np.sqrt(2), x_arr))[0]))
plt.savefig("ep3_difference.png")
