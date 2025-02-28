import matplotlib.pyplot as plt
import numpy as np

x_points=np.array([0,6])
y_points=np.array([0,100])
plt.plot(x_points, y_points)
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()