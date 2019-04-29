import matplotlib.pyplot as plt

P = 17


x = []
y = []

for i_x in range(P):
    for i_y in range(P):
        if ((i_x**3 + 7)-(i_y**2)) % P == 0:
            x.append(i_x)
            y.append(i_y)

plt.scatter(x, y)
plt.show()

