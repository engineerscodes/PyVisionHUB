import os.path

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator

Base_dir = 'cats_and_dogs'

train_dir = os.path.join(Base_dir, 'train')
validation_dir = os.path.join(Base_dir, 'validation')

dog_train_dir = os.path.join(train_dir, 'dogs')
cat_train_dir = os.path.join(train_dir, 'cats')

validation_cats_dir = os.path.join(validation_dir, 'cats')
validation_dogs_dir = os.path.join(validation_dir, 'dogs')

num_train_cat = len(os.listdir(cat_train_dir))
num_train_dog = len(os.listdir(dog_train_dir))

num_val_dog = len(os.listdir(validation_dogs_dir))
num_val_cat = len(os.listdir(validation_cats_dir))

print(f"No of training cat : {num_train_cat}\nNo of training Dog : {num_train_dog}"
      f"\nNo of Validation Set(Cat) : {num_val_cat}"
      f"\nNo of Validation Set(Dog) : {num_val_dog}")

# Model Parameters
Batch_Size = 32
New_Img_Size = (150, 150)

# DATA PREPROCESSING

# normalizing pixel value from 0 -255 => TO 0-1
'''
Images must be formatted into appropriately pre-processed floating point 
tensors before being fed into the network. The steps involved in preparing these images are:
Read images from the disk
Decode contents of these images and convert it into proper grid format as per their RGB content
Convert them into floating point tensors
Rescale the tensors from values between 0 and 255 to values between 0 and 1, as neural networks prefer to deal with small input values.
'''
train_img_generator = ImageDataGenerator(rescale=1.0 / 255)
validation_img_generator = ImageDataGenerator(rescale=1.0 / 255)

# Since Img size is not fixed we have to resize img to fixed size before feeding into NN

# resize img

train_data = train_img_generator.flow_from_directory(batch_size=Batch_Size,
                                                     directory=train_dir,
                                                     shuffle=True,
                                                     target_size=New_Img_Size,
                                                     class_mode='binary')
validation_data = validation_img_generator.flow_from_directory(batch_size=Batch_Size,
                                                               directory=validation_dir,
                                                               shuffle=False,
                                                               target_size=New_Img_Size,
                                                               class_mode='binary')

sample_data, _ = next(train_data)


def plot(img_src):
    fig, axes = plt.subplots(1, 5, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(img_src, axes):
        ax.imshow(img)
    plt.tight_layout()
    plt.show()


plot(sample_data[:5])

# Model Creation
# input image - 150*150 px with 3 channels (RGB)
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation=tf.nn.relu, input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPool2D(2, 2),

    tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation=tf.nn.relu),
    tf.keras.layers.MaxPool2D(2, 2),

    tf.keras.layers.Conv2D(128, kernel_size=(3, 3), activation=tf.nn.relu),
    tf.keras.layers.MaxPool2D(2, 2),

    tf.keras.layers.Conv2D(128, kernel_size=(3, 3), activation=tf.nn.relu),
    tf.keras.layers.MaxPool2D(2, 2),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(2, activation=tf.nn.softmax)  # two classes DOG/CAT

])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

print(model.summary())

total_train = num_train_dog + num_train_cat
total_val = num_val_cat + num_val_dog

EPOCH = 20

history = model.fit_generator(
    generator=train_data,
    steps_per_epoch=int(np.ceil(total_train / float(Batch_Size))),
    epochs=EPOCH,
    validation_data=validation_data,
    validation_steps=int(np.ceil(total_val / float(Batch_Size)))
)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(EPOCH)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.savefig('./foo.png')
plt.show()

# MODEL IS OVERFITTING
"""
Because - ------------ - - - - ->>>>

Epoch 19/20
63/63 [==============================] - 53s 832ms/step - loss: 3.4270e-04 - accuracy: 1.0000 - val_loss: 1.8601 - val_accuracy: 0.7310
Epoch 20/20
63/63 [==============================] - 59s 937ms/step - loss: 2.4248e-04 - accuracy: 1.0000 - val_loss: 1.9137 - val_accuracy: 0.7310
"""

# PREVENT OVERFITTING

"""
Other Techniques to Prevent Overfitting
In this lesson we saw three different techniques to prevent overfitting:

1) Early Stopping: In this method, we track the loss on the validation 
set during the training phase and use it to determine 
when to stop training such that the model is accurate but not overfitting.

2) Image Augmentation: Artificially boosting the number of images in our 
training set by applying random image transformations to the existing images in the training set.

3) Dropout: Removing a random selection of a fixed number of neurons in a 
neural network during training.
However, these are not the only techniques available to prevent overfitting.
You can read more about these and other techniques in the link below:

"""