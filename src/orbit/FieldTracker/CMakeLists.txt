include_directories(${CMAKE_CURRENT_SOURCE_DIR})

file(GLOB src_files wrap_*.cc)

add_library(fieldtracker MODULE  ${src_files})
python_extension_module(fieldtracker)
target_link_libraries(fieldtracker pyorbit)
install(TARGETS fieldtracker LIBRARY DESTINATION py/orbit/mod)
