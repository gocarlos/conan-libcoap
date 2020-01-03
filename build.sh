#!/bin/bash

# normal compilation
export CC=gcc-9
export CXX=g++-9
conan create . gocarlos/testing --build missing
