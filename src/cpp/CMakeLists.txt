add_library(sourceLibrary
    main.cpp
    load.cpp
)

add_subdirectory(simpleFlow)
add_subdirectory(lib)

# Adding current directory to include path
target_include_directories(simpleFlowLibrary PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
