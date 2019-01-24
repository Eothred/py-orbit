cmake_minimum_required(VERSION 3.0)

PROJECT(pyorbit C CXX)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/modules")

find_package(PythonExtensions REQUIRED)

add_subdirectory(src)
