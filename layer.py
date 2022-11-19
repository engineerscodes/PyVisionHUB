import numpy as np

inputs = [1, 2, 3.5, 6]

weights = [[0.2, -1, 0.9, -9],
           [.5, 9, -4, 1.8],
           [1, 3, -0.45, 9]]

biases = [2, 3, -1]

layer_output = []
for neuron_wei, bias in zip(weights, biases):
    neuron_output = 0
    for n_inputs, weight in zip(inputs, neuron_wei):
        neuron_output += n_inputs * weight
    neuron_output += bias
    layer_output.append(neuron_output)

print(layer_output)

a = [1, 2, 3]
b = [2, 3, 4]
dot_product = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
print(dot_product)

dot_product = np.dot(inputs, weights[0]) +biases[0]
# this is like line equation y=mx +c
# and u can see how different weights  impact the line equation
# my changing bias we can move line up & down 
# https://www.youtube.com/watch?v=tMrbN67U9d4
print(dot_product)

# a simple value to do this is
dot_product = np.dot(weights,inputs)+biases
print(f"this works {dot_product}")

# but if u interchange weight & inputs it will not work
# Because of implementation of numpy the first arg must be matrix and second a vector so that it can return
# an array
dot_product = np.dot(inputs,weights)+biases
print(f"this will not  works {dot_product}")

