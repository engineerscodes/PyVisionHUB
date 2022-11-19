"""
softmax function is used to normalize the outputs, 
converting them from weighted sum values into probabilities that sum to one. 
Each value in the output of the softmax function 
is interpreted as the probability of membership for each class
"""

import math
import numpy as np
from Batch import *

E = math.e

layer_outputs = [4.8, 1.21, 2.385]
exp_values = []

for output in layer_outputs:
    exp_values.append(E ** output)

print(exp_values)

# normalization
norm = sum(exp_values)
norm_value = []

for value in exp_values:
    norm_value.append(value / norm)

print(norm_value)

# numpy

exp_values = np.exp(layer_outputs)
norm_value = exp_values / np.sum(exp_values)
print(norm_value)


# the combination of exponential & normalize is softmax

# the issue with exponential cal is that it run to overflow ex -np.exp(1000)

# to prevent this we have to subtract all value with max(value) from the layer
# now r range of value -(infinity to 0)

class ActivationSoftmax:

    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities


x, y = createData(100, 3)
layer_1 = LayerDense(2, 3)
relu = ActivationRELU()
layer_2 = LayerDense(3, 3)
softmax = ActivationSoftmax()

layer_1.forward(x)
relu.forward(layer_1.output)
layer_2.forward(relu.output)
softmax.forward(layer_2.output)

print(softmax.output)

