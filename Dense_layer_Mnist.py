import tensorflow as tf
import tensorflow_datasets as tfds
import math
import numpy as np
import matplotlib.pyplot as plt

# image classification of Clothing
# https://colab.research.google.com/github/tensorflow/examples/blob/master/
# courses/udacity_intro_to_tensorflow_for_deep_learning/l03c01_classifying_images_of_clothing.ipynb#scrollTo=oSzE9l7PjHx0

data, meta_data = tfds.load('fashion_mnist', as_supervised=True, with_info=True)
train_dataset, test_dataset = data['train'], data['test']

class_names = meta_data.features['label'].names
print(class_names)

num_train_examples = meta_data.splits['train'].num_examples
num_test_examples = meta_data.splits['test'].num_examples
print("Number of training examples: {}".format(num_train_examples))
print("Number of test examples:     {}".format(num_test_examples))


# The map function applies the normalize function to each element in the train
# and test datasets
def normalize(images, labels):
    images = tf.cast(images, tf.float32)
    images /= 255
    return images, labels


train_dataset = train_dataset.map(normalize)
test_dataset = test_dataset.map(normalize)

# The first time you use the dataset, the images will be loaded from disk
# Caching will keep them in memory, making training faster
train_dataset = train_dataset.cache()
test_dataset = test_dataset.cache()

plt.figure(figsize=(10, 10))
for i, (image, label) in enumerate(train_dataset.take(25)):
    image = image.numpy().reshape((28, 28))
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(image, cmap=plt.cm.binary)
    plt.xlabel(class_names[label])
plt.show()

# BUILD MODEL
'''
input tf.keras.layers.Flatten — This layer transforms the images from a 2d-array of 28  ×  28 pixels,
to a 1d-array of 784 pixels (28*28). Think of this layer as unstacking rows of pixels in the image and lining them up.
This layer has no parameters to learn, as it only reformats the data.

"hidden" tf.keras.layers.Dense— A densely connected layer of 128 neurons. 
Each neuron (or node) takes input from all 784 nodes in the previous layer, 
weighting that input according to hidden parameters which will be learned during training,
and outputs a single value to the next layer.
'''
layer_0 = tf.keras.layers.Flatten(input_shape=(28, 28, 1))
layer_1 = tf.keras.layers.Dense(units=128, activation=tf.nn.relu)
layer_2 = tf.keras.layers.Dense(units=10, activation=tf.nn.softmax)
# 10 units because output has 10 classes

model = tf.keras.Sequential([layer_0, layer_1, layer_2])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

BATCH_SIZE = 32
train_dataset = train_dataset.cache().repeat().shuffle(num_train_examples).batch(BATCH_SIZE)
test_dataset = test_dataset.cache().batch(BATCH_SIZE)
# The epochs=5 parameter limits training to 5 full iterations of the training dataset,
# so a total of 5 * 60000 = 300000 examples
model.fit(train_dataset, epochs=5, steps_per_epoch=math.ceil(num_train_examples / BATCH_SIZE))

test_loss, test_accuracy = model.evaluate(test_dataset, steps=math.ceil(num_test_examples / 32))
print('Accuracy on test dataset:', test_accuracy)

for test_images, test_labels in test_dataset.take(1):
    test_images = test_images.numpy()
    test_labels = test_labels.numpy()
    predictions = model.predict(test_images)
    print(predictions)
