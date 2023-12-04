#ifndef LAYER_HPP
#define LAYER_HPP

#include <string>

class Layer {
public:
    Layer(const std::string& name) : name(name) {}

protected:
    std::string name;
};

#endif