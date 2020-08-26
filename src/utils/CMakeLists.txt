include_directories(statistics)

file(GLOB src_files wrap_*.cc */wrap_*.cc)

add_library(orbit_utils MODULE  ${src_files})
python_extension_module(orbit_utils)
target_link_libraries(orbit_utils pyorbit)
install(TARGETS orbit_utils LIBRARY DESTINATION py/orbit/mod)
