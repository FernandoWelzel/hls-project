add_library(sourceLibrary
    main.cpp
)

add_subdirectory(simpleFlow)

# Building main executable
add_executable(project main.cpp)
target_link_libraries(project PRIVATE sourceLibrary simpleFlowLibrary)
