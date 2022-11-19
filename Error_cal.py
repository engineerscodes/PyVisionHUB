"""
Categorical crossentropy is a loss function that is used in multi-class classification tasks.
These are tasks where an example can only belong to one out of many possible categories,
and the model must decide which one. Formally, it is designed to quantify the difference between
two probability distributions.
"""

'''ONE HOT ENCODING'''
import math

softmax_output = [0.7, 0.1, 0.2]
target_output = [1, 0, 0]

loss = -(math.log(softmax_output[0]) * target_output[0] +
         math.log(softmax_output[1]) * target_output[1] +
         math.log(softmax_output[2]) * target_output[2])

print(loss)