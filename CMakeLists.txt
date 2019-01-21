cmake_minimum_required(VERSION 3.0)

PROJECT(pyorbit CXX)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/modules")

add_subdirectory(src)
