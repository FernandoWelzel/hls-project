add_library(simpleFlowLibrary
    CONV2D.cpp
)

target_include_directories(simpleFlowLibrary PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})