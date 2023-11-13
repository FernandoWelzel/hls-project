# Base model

# model = tf.keras.Sequential([
#     tfLayers.Conv2D(64, (3, 3), activation='relu', input_shape=(24, 24, 3), padding='same', name='conv1'),
#     tfLayers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='same'),

#     tfLayers.Conv2D(32, (3, 3), activation='relu', input_shape=(12, 12, 64), padding='same', name='conv2'),
#     tfLayers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='same'),

#     tfLayers.Conv2D(20, (3, 3), activation='relu', input_shape=(6, 6, 32), padding='same', name='conv3'),
#     tfLayers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='same'),

#     tfLayers.Reshape((-1, 180)),

#     tfLayers.Dense(10, name='local3')
# ])
