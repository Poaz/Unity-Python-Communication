"""
pip install tensorflow keras gym



"""
from keras.models import Model
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense
from keras.datasets import mnist
from keras.utils import to_categorical

def model(num_classes, input_shape):

    input = Input(shape=input_shape)

    x = Conv2D(filters=16, kernel_size=(3,3), strides=(1,1), activation='relu')(input)
    x = MaxPooling2D()(x)
    x = Flatten()(x)
    x = Dense(num_classes, activation='softmax')(x)

    model = Model(inputs=input, outputs=x)

    return model


(x_train, y_train), (x_test, y_test) = mnist.load_data('mnistdata.npz')

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

img_rows, img_cols = 28, 28

x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

input_shape = (img_rows, img_cols, 1)

model = model(10, input_shape)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()
#from keras.callbacks import EarlyStopping
#e = EarlyStopping()
model.fit(x_train, y_train, epochs=10, batch_size=256, validation_data=(x_test, y_test))







