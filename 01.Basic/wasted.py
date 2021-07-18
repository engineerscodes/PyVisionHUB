'''
Consider the following numpy array:

import numpy as np
x = np.arange(10,21)

i)   What will be the output of the following commands:
a)      print(x)
b)     print(x[-3])
c)      print[x[-4,:])

ii)  Write the command to print all elements from index 1 to index 9 with a difference of 2.
iii)  Write the command to print all elements from index 7 to index 2 using negative indexing.
'''

import numpy as np
x = np.arange(10,21)

print(x)
print(x[-3])
#print(x[-4,:])

print(x[1:9 :2])

print(x[7:1:-1])