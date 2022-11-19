# single Neuron

inputs = [1, 2, 5.6]
weight = [3, 5, 8.9]
basis = 6

output = 0

for i in range(0, len(inputs)):
    output += inputs[i] * weight[i]

output += basis
print(output)
