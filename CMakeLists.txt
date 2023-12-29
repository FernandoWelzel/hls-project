cmake_minimum_required(VERSION 3.11)

project(3A-SEI-SoC-HLS-PROJECT)

set(CMAKE_BUILD_TYPE Debug)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -Wconversion -std=gnu99")

# Enabling unit testing
enable_testing()

# Adding directories
add_subdirectory(src)
add_subdirectory(test)

# Building main executable
add_executable(project src/cpp/main.cpp)
target_link_libraries(project PRIVATE sourceLibrary simpleFlowLibrary)

# Making test data available at this folder
file(COPY data/processed DESTINATION ${CMAKE_CURRENT_BINARY_DIR})