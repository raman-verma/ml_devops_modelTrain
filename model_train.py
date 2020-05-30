import numpy as np
from keras.utils.np_utils import to_categorical # convert to one-hot-encoding
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D
from keras.optimizers import Adam

from keras.datasets import mnist
dataset = mnist.load_data('mymnist.db')

# data set contani both the things
# Traing data
# Test data
train, test = dataset
X_train, y_train = train
X_test, y_test = test

# Reshaping the the data for making it fit for the model traning.
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)


# we use the standard initialization methods for weights, 
# however, data between 0 and 1 should make the net converge faster.
X_train = X_train.astype("float32")/255.
X_test = X_test.astype("float32")/255.

# using one hot encoding for categorial data
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Start building the model
model = Sequential()

model.add(Conv2D(filters = 32, kernel_size = (3, 3), activation='relu',
                 input_shape = (28, 28, 1)))
model.add(MaxPool2D(strides=(2,2)))

# model.add(Conv2D(filters = 32, kernel_size = (3, 3), activation='relu'))
# model.add(Conv2D(filters = 32, kernel_size = (3, 3), activation='relu'))


model.add(Flatten())
model.add(Dense(units=512, activation='relu'))
model.add(Dense(units=1024, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

print(model.summary())

model.compile(loss='categorical_crossentropy', optimizer = Adam(lr=1e-4), metrics=["accuracy"])

hist = model.fit(X_train, y_train, epochs=1)

# save the model
model.save("mnist_LeNet.h5")

# Evaluate the performance of our trained model
final_loss, final_acc = model.evaluate(X_test, y_test, verbose=1)
print("Final loss: {0:.4f}, final accuracy: {1:.4f}".format(final_loss, final_acc))

f=open("accuracy","w")
f.write("{}".format(model.history.history['accuracy'][-1]))
f.close()

r=open("history","a")
r.write('Test loss: {}'.format(str(final_loss)))
r.write('\nTest accuracy: {}'.format(str(final_acc)))
r.close()