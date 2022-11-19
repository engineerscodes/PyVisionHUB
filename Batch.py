"""
In practical terms, to determine the optimum batch size, we recommend trying
smaller batch sizes first(usually 32 or 64), also keeping in mind that small batch sizes
require small learning rates. The number of batch sizes should be a power of 2 to
take full advantage of the GPUs processing.


It is a way of Training your Neurons
if batch size is one you are training neuron with one set of input
which is not good because it has to change weight and bias again for next inputs
if batch size 32 that means your train you neuron for every 32 set of inputs

"""
import numpy as np
import matplotlib.pyplot as plt

inputs = [
    [1, 2, 3, .25],
    [2.0, 5.0, 1.0, 0.5],
    [-0.26, -0.27, 0.17, 0.87]
]

weight = [[0.2, 5.9, 8.2, 8],
          [9.0, -4, -0.5, 9],
          [0.1, 0.5, -9, -.099]
          ]

biases = [1, 2, 3]
# to make matrix multiplication u need to take transpose of weight matrix
# if not then shapes (3,4) and (3,4) not aligned: 4 (dim 1) != 3 (dim 0)
# because to multiply your m1.c=m2.r
#   [1, 2, 3, .25] * [0.2, 5.9, 8.2, 8] Transpose
layer_1 = np.dot(inputs, np.array(weight).T) + biases
print(layer_1)

# layer 2
biases_2 = [-.9, -5, 9]

weight_2 = [
    [0.1, 0.5, 2],
    [-0.5, 5, 9],
    [-0.44, 8, 9]
]

layer_2 = np.dot(layer_1, np.array(weight_2).T) + biases_2

print(layer_2)


# class Implementation

class LayerDense:

    # no of neurons & no of weights
    def __init__(self, n_weights, n_neurons):
        self.weight = 0.10 * np.random.rand(n_weights, n_neurons)  # row,col
        self.biases = np.zeros(shape=(1, n_neurons))  # 1 row & n_neurons of  col

    def forward(self, inputs):
        # no need for Transpose because it already
        self.output = np.dot(inputs, self.weight) + self.biases


class ActivationRELU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


layer_1 = LayerDense(4, 5)
# since it will create 4*5 matrix and output will be  4*5 since it will be input to next
# layer 2 it be (5,X) size
layer_2 = LayerDense(5, 6)

layer_1.forward(inputs)
print("Output ")
print(layer_1.output)  # 3*4 into 4*5 ==> output of layer 1 is 3*5

layer_2.forward(layer_1.output)
print("Layer 2\n", layer_2.output)


# Hidden Layer Activation Functions

# 1) STEP FUNCTION -> Zero or 1
# 2) SIGMOID FUNCTION
# 3) RELU FUNCTION faster because unlike sigmoid because formula is f(x)=x ,x>0 && f(x)=0 ,x<0 cal is fast

# https://www.youtube.com/watch?v=gmjzbpSVY1A&t=2s IMP

def createData(points, classes):
    x = np.zeros((points * classes, 2)) # to features
    y = np.zeros(points * classes, dtype='uint8')

    for class_num in range(classes):
        ix = range(points * class_num, points * (class_num+ 1))
        r = np.linspace(0.01, 1, points)
        t = np.linspace(class_num * 4, (class_num + 1) * 4, points) + np.random.randn(points) * 0.2
        # add along second axis.
        x[ix] = np.c_[r * np.sin(t * 2.5), r * np.cos(t * 2.5)]
        y[ix] = class_num

    return x, y


x, y = createData(100, 3)


plt.scatter(x[:,0],x[:,1],c=y,cmap="brg")
plt.show()

layer_1 = LayerDense(2, 5) # no of inputs . no of neurons
RELU = ActivationRELU()
layer_1.forward(x)
RELU.forward(layer_1.output)

print(RELU.output) # since RELU ALL NEGATIVE VALUE WILL BE ZERO NOW


