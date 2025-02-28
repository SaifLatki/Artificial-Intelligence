import matplotlib.pyplot as plt
import numpy as np

home_sizes=np.array([120,150,200,250,300,400,600])
home_prices=np.array([0.5,1.0,1.2,1.5,2.0,3.0,5.0])

plt.plot(home_sizes,home_prices,marker='*' ,linestyle='-')
plt.title('Home Prices vs Sizes')
plt.xlabel('Home Sizes (sq ft)')
plt.ylabel('Home Prices (in $ millions)')
plt.grid(True)
plt.show()