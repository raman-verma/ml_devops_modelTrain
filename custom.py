

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

hist = model.fit(X_train, y_train, epochs=3)

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