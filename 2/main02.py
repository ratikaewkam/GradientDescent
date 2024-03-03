import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return np.sin(2*x) * np.cos(2*y) / 2

def gradient(x, y):
    return np.cos(2*x) * np.cos(2*y), -np.sin(2*x) * np.sin(2*y)

x = np.arange(-1.2, 1.2, 0.01)
y = np.arange(-1.2, 1.2, 0.01)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
x_point = 0.625
y_point = 0.1
pos = (x_point, y_point, f(x_point, y_point))
alpha = 0.05
round = 1000

ax = plt.subplot(projection="3d", computed_zorder=False)

for i in range(round):
        x_derivative, y_derivative = gradient(pos[0], pos[1])
        new_x, new_y = pos[0] - alpha * x_derivative, pos[1] - alpha * y_derivative
        pos = new_x, new_y, f(new_x, new_y)

        ax.plot_surface(X, Y, Z, cmap="viridis", zorder=0)
        ax.scatter(pos[0], pos[1], pos[2], color="red", zorder=1)
        plt.pause(0.001)
        ax.clear()

ax.plot_surface(X, Y, Z, cmap="viridis", zorder=0)
ax.scatter(x_point, y_point, gradient(x_point, y_point), color="black", zorder=1)
ax.scatter(pos[0], pos[1], pos[2], color="red", zorder=1)
plt.show()

print(pos)