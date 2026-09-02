import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.exp(x**2)
print(f(0))
xx=np.linspace(-1.1,1.1,100)
plt.plot(xx, f(xx))
plt.show()
