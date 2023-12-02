import numpy as np
import pytest
import simpleFlow as sf

# Convoltional tests
@pytest.fixture
def conv_model():
    return sf.Conv2D(kernel_size=(3, 3), output_shape=(1, 5, 5), input_shape=(1, 5, 5), name="conv1")

@pytest.fixture
def test_matrix_conv():
    return np.array((
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    ))

@pytest.fixture
def result_matrix_conv():
    return np.array((
        [ 7, 13, 19, 25, 19],
        [10, 19, 28, 37, 28],
        [10, 19, 28, 37, 28],
        [10, 19, 28, 37, 28],
        [ 7, 13, 19, 25, 19]
    ))

def test_conv_forward(conv_model, test_matrix_conv, result_matrix_conv):
    result = conv_model.forward(test_matrix_conv)

    # Compares all elements of the expected conv matrix
    assert((result == result_matrix_conv).all())

# Dense layer tests
@pytest.fixture
def dense_model():
    return sf.Dense(output_size=5, input_size=5, name="dense1")

@pytest.fixture
def test_matrix_dense():
    return np.array((
        [1, 2, 3, 4, 5]
    ))

@pytest.fixture
def result_matrix_dense():
    return np.array((
        [16, 16, 16, 16, 16]
    ))

def test_dense_forward(dense_model, test_matrix_dense, result_matrix_dense):
    result = dense_model.forward(test_matrix_dense)

    assert((result == result_matrix_dense).all())

# Pooling layer test
@pytest.fixture
def pool_model():
    return sf.MaxPooling2D(input_shape=(1, 5, 5), strides=(1, 1), pool_size=(3, 3), name="pool1")

@pytest.fixture
def result_matrix_pool():
    return np.array((
        [3, 4, 5, 5, 5],
        [3, 4, 5, 5, 5],
        [3, 4, 5, 5, 5],
        [3, 4, 5, 5, 5],
        [3, 4, 5, 5, 5]
    ))

def test_pool_forward(pool_model, test_matrix_conv, result_matrix_pool):
    result = pool_model.forward(test_matrix_conv)

    assert((result == result_matrix_pool).all())

# Running all tests
if __name__ == "__main__":
    pytest.main()