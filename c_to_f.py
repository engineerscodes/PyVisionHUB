import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

celsius_q = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit_a = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

ele = zip(celsius_q, fahrenheit_a)

for c, f in ele:
    print(c, f)

# https://colab.research.google.com/github/tensorflow/examples/blob/master/courses/
# udacity_intro_to_tensorflow_for_deep_learning/l02c01_celsius_to_fahrenheit.ipynb#scrollTo=VM7_9Klvq7MO
# sice it a simple problem on layer is enough  - and one neuron
# eq = w1*x + b = x(1.8)+32

layer_0 = tf.keras.layers.Dense(units=1, input_shape=[1])

model = tf.keras.Sequential(layers=[layer_0])

# loss fn - mean_squared_error
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))  # 0.1 is learning rate

# train model
history = model.fit(x=celsius_q, y=fahrenheit_a, epochs=500, verbose=False)
print("Finished training the model")
# The epochs argument specifies how many times this cycle should be run,
# and the verbose argument controls how much output the method produces.

# Display statics
plt.xlabel('Epoch Number')
plt.ylabel("Loss Magnitude")
plt.plot(history.history['loss'])
plt.show()
# predict values
print(model.predict([100.0]))  # 100×1.8+32=212
# We created a model with a Dense layer
# We trained it with 3500 (7 INPUTS * epochs=500) examples (7 pairs, over 500 epochs).

print(f"Model weight : {model.layers[0].weights} \nModel Bias: {model.layers[0].bias.numpy()}")
# y = 1.82227 * x +29.10348

# with mutiple layers
