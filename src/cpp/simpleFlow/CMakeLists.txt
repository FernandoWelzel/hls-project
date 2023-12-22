add_library(simpleFlowLibrary
    conv2d.cpp
    load.cpp
)

target_include_directories(simpleFlowLibrary PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})