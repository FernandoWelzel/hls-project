import pickle

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='latin1')
    return dict

File = "../../../cifar-10-python/cifar-10-batches-py/data_batch_1"
data_batch_1 = unpickle(File)
print(type(data_batch_1))
print(data_batch_1.keys())

X_train = data_batch_1['data']

meta_file = "../../../cifar-10-python/cifar-10-batches-py/batches.meta"
meta_data = unpickle(meta_file)
print(type(meta_data))
print(meta_data.keys()) 

print("Label Names:", meta_data['label_names'] )


image = data_batch_1['data'][0]

image = image.reshape(3,32,32)
print(image.shape)

image = image.transpose(1,2,0)
print(image.shape)

X_train = data_batch_1['data']
print("Shape before reshape:", X_train.shape)
# Reshape the whole image data
X_train = X_train.reshape(len(X_train),3,32,32)
print("Shape after reshape and before transpose:", X_train.shape)
# Transpose the whole data
X_train = X_train.transpose(0,2,3,1)
print("Shape after reshape and transpose:", X_train.shape)

import matplotlib.pyplot as plt
# label names
label_name = meta_data['label_names']
# take first image
image1 = data_batch_1['data'][0]
# take first image label index
label = data_batch_1['labels'][0]
# Reshape the image
image2 = image1.reshape(3,32,32)
# Transpose the image
image3 = image2.transpose(1,2,0)
# Display the image
plt.imshow(image3)
# plt.title(label_name[label])
plt.show()