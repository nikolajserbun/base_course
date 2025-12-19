import matplotlib.pyplot as plt

x = [3, 8, 5]
y = [7, 4, 9]

plt.xkcd()

plt.plot(x, y, color='g', lable='Graf 1', marker='>', ms=5)
plt.plot(x, y, color='r', lable='Graf 2', marker='>', ms=3)

#Украшательства:
plt.xlabel('Coord: x')
plt.ylabel('Coord: y')
plt.legend()
plt.title('Base')
plt.grid()
plt.savefig('fig_2.png')

