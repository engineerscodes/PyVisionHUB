import os.path

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator

# Dogs vs Cats Image Classification With Image Augmentation
# https://colab.research.google.com/github/tensorflow/examples/
# blob/master/courses/udacity_intro_to_tensorflow_for_deep_learning/l05c02_dogs_vs_cats_with_augmentation.ipynb


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

# rotation of 45 degrees, width shift, height shift, horizontal flip, and zoom augmentation to our training images.
train_img_generator = ImageDataGenerator(rescale=1. / 255,
                                         rotation_range=45,
                                         width_shift_range=0.2,
                                         height_shift_range=0.2,
                                         shear_range=0.2,
                                         zoom_range=0.2,
                                         horizontal_flip=True,
                                         fill_mode='nearest')
validation_img_generator = ImageDataGenerator(rescale=1.0 / 255)

train_data_gen = train_img_generator.flow_from_directory(batch_size=Batch_Size,
                                                         directory=train_dir,
                                                         shuffle=True,
                                                         target_size=New_Img_Size,
                                                         class_mode='binary')

augmented_images = [train_data_gen[0][0][0] for i in range(5)]


def plotImages(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
    plt.tight_layout()
    plt.show()


plotImages(augmented_images)

image_gen_val = ImageDataGenerator(rescale=1. / 255)

val_data_gen = image_gen_val.flow_from_directory(batch_size=Batch_Size,
                                                 directory=validation_dir,
                                                 target_size=New_Img_Size,
                                                 class_mode='binary')

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

    tf.keras.layers.Dropout(0.5),
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
    generator=train_data_gen,
    steps_per_epoch=int(np.ceil(total_train / float(Batch_Size))),
    epochs=EPOCH,
    validation_data=val_data_gen,
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
plt.show()

'''
20/20 [==============================] - 17s 843ms/step - loss: 0.2673 - accuracy: 0.8835 - val_loss: 0.3671 - val_accuracy: 0.8450
Epoch 100/100
20/20 [==============================] - 17s 868ms/step - loss: 0.2726 - accuracy: 0.8795 - val_loss: 0.3692 - val_accuracy: 0.8550
'''