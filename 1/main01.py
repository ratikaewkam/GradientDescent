import gradient_descent_a as gd
import numpy as np

def f(x):
    return np.power(((x/7) - 2), 2) + 5

def f_derivative(x):
    return (2*x/49) - 4/7

x = np.arange(-200, 200)
y = f(x)
point = -200
pos_now = (point, f(point))
alpha = 0.15
round = 2500

data = gd.gd(x, y, pos_now, alpha, round, f, f_derivative)
print(data)