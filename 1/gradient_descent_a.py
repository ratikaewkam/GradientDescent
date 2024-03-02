import matplotlib.pyplot as plt

def gd(x, y, pos, alpha, round, f, f_derivative):
    for i in range(round):
        new_x = pos[0] - alpha * f_derivative(pos[0])
        new_y = f(new_x)
        pos = (new_x, new_y)

        plt.xlabel("x")
        plt.ylabel("y")
        plt.plot(x, y)
        plt.scatter(pos[0], pos[1], color="red")
        plt.pause(0.001)
        plt.clf()

    return pos