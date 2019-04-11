import numpy as np
import matplotlib.pyplot as plt

def fun (t):
	if 10 <= t < 12:
		return (t-10)*(t-10)*0.25
	elif 12 <= t < 14:
		return (1.5 - 0.5*(t-13)*(t-13))
	elif 14 <= t < 16:
		return (t-16)*(t-16)*0.25
	return 0.0

vfun = np.vectorize(fun)

x = np.linspace(0, 18, 1000)    
y = vfun(x)

plt.ylim([0, 1.6])
plt.plot(x, y, '-')
plt.title('Problem 4 graph')
plt.xlabel('t')
plt.ylabel('c(t)')
plt.show()