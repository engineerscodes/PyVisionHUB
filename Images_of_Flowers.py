import os.path
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
import shutil
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D

#  Classify Images of Flowers

'''
flower_photos
|__ daisy
|__ dandelion
|__ roses
|__ sunflowers
|__ tulips
since there is No train / val we need to create folder
'''

base_dir = os.path.join("C:\\Users\\NAVEEN\\Downloads\\flower_photos", 'flower_photos')

classes = ['roses', 'daisy', 'dandelion', 'sunflowers', 'tulips']

for className in classes:
    path = os.path.join(base_dir, className)
    print(path)
    files = os.listdir(path)
    num_files = len(files)
    print(num_files)
    split = int((num_files * 80.0) / 100)
    train_set, val_set = files[:split], files[split:]

    for t_f in train_set:
        if not os.path.exists(os.path.join(base_dir, 'train', className)):
            os.makedirs(os.path.join(base_dir, 'train', className))
        shutil.move(os.path.join(path, t_f), os.path.join(base_dir, 'train', className))
    for v_f in val_set:
        if not os.path.exists(os.path.join(base_dir, 'val', className)):
            os.makedirs(os.path.join(base_dir, 'val', className))
        shutil.move(os.path.join(path, v_f), os.path.join(base_dir, 'val', className))

train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'val')
num_train = len(os.listdir(train_dir))
num_val = len(os.listdir(validation_dir))

Batch_size = 100
New_Img_Size = (150, 150)

image_gen_train = ImageDataGenerator(rescale=1. / 255,
                                     rotation_range=40,
                                     width_shift_range=.15,
                                     height_shift_range=.15,
                                     horizontal_flip=True,
                                     zoom_range=0.5)

train_data_gen = image_gen_train.flow_from_directory(batch_size=Batch_size ,
                                                     directory=train_dir,
                                                     shuffle=True,
                                                     target_size=New_Img_Size,
                                                     class_mode='sparse')


def plotImages(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
    plt.tight_layout()
    plt.show()


augmented_images = [train_data_gen[0][0][0] for i in range(5)]
plotImages(augmented_images)

image_gen_val = ImageDataGenerator(rescale=1. / 255)

val_data_gen = image_gen_val.flow_from_directory(batch_size=Batch_size,
                                                 directory=validation_dir,
                                                 target_size=New_Img_Size,
                                                 class_mode='sparse')

model = tf.keras.Sequential()
model.add(Conv2D(16, 3, padding='same', activation='relu', input_shape=(150, 150, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, 3, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, 3, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))

model.add(Dropout(0.2))
model.add(Dense(5, activation=tf.nn.softmax))

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

epochs = 80

history = model.fit_generator(
    generator=train_data_gen,
    steps_per_epoch=int(np.ceil(train_data_gen.n / float(Batch_size))),
    epochs=epochs,
    validation_data=val_data_gen,
    validation_steps=int(np.ceil(val_data_gen.n / float(Batch_size)))
)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

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