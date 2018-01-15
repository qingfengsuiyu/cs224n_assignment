
import numpy as np 

# A
x = np.random.random(100000)

def sigmoid(x):
	return 1/(1+np.exp(-x))

print(sigmoid(x))

c = x + 0.2

print(sigmoid(x))


# B

a = np.matrix('1,2;3,4;5,6;7,8')
print(sigmoid(a))