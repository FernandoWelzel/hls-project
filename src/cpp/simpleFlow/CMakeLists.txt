add_library(simpleFlowLibrary
    CONV2D.cpp
    POOL2D.cpp
    DENSE.cpp
    TOP.cpp
    load.cpp
)

target_include_directories(simpleFlowLibrary PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})