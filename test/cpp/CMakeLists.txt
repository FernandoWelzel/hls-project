# Convolutional test
add_executable(conv2_test conv2_test.cpp)
target_link_libraries(conv2_test PRIVATE gtest_main sourceLibrary simpleFlowLibrary)
add_test(conv2_test conv2_test)
