# previously we solved using A dense Layer now we will be using CNN
# https://learn.udacity.com/courses/ud187/lessons/
# cbb8612c-cd13-4994-8029-1e373f5b42dc/concepts/a3dd8997-0498-44f3-a901-2fb42298b2d2

import tensorflow as tf
import tensorflow_datasets as tfds
import math
import matplotlib.pyplot as plt

# https://colab.research.google.com/github/tensorflow/examples/blob/
# master/courses/udacity_intro_to_tensorflow_for_deep_learning/l04c01_image_classification_with_cnns.ipynb#scrollTo=Gxg1XGm0eOBy

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

'''
The basic building block of a neural network is the layer.
A layer extracts a representation from the data fed into it. Hopefully, a series of 
connected layers results in a representation that is meaningful for the problem at hand.
Much of deep learning consists of chaining together simple layers. Most layers, like tf.keras.layers.Dense, 
have internal parameters which are adjusted ("learned") during training.
'''
# kernel = fiter
# 32 number of filters/kernel of size 3,3 
layer_0 = tf.keras.layers.Conv2D(32, kernel_size=(3, 3), padding='same', activation=tf.nn.relu)
layer_1 = tf.keras.layers.MaxPool2D((2, 2), strides=2)
layer_2 = tf.keras.layers.Conv2D(64, (3, 3), padding="same", activation=tf.nn.relu)
layer_3 = tf.keras.layers.MaxPool2D((2, 2), strides=2)
layer_4 = tf.keras.layers.Flatten()
layer_5 = tf.keras.layers.Dense(128, activation=tf.nn.relu)
layer_6 = tf.keras.layers.Dense(10, activation=tf.nn.softmax)

model = tf.keras.Sequential([layer_0, layer_1, layer_2, layer_3, layer_4, layer_5, layer_6])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

BATCH_SIZE = 32
train_dataset = train_dataset.cache().repeat().shuffle(num_train_examples).batch(BATCH_SIZE)
test_dataset = test_dataset.cache().batch(BATCH_SIZE)

history = model.fit(train_dataset, epochs=10, steps_per_epoch=math.ceil(num_train_examples / BATCH_SIZE))
test_loss, test_accuracy = model.evaluate(test_dataset, steps=math.ceil(num_test_examples / 32))
print('Accuracy on test dataset:', test_accuracy)
print("Plotting ...............")
plt.xlabel('Epoch Number')
plt.ylabel("Loss Magnitude")
plt.plot(history.history['loss'])
plt.show()

# accuracy is 91%
# the accuracy is low because we are overfitting model we have to decease epoch
