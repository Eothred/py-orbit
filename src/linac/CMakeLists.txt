include_directories(${CMAKE_CURRENT_SOURCE_DIR})

#add_subdirectory(rfgap)
add_subdirectory(tracking)

include_directories(rfgap)
include_directories(tracking)

file(GLOB src_files wrap_*.cc)

add_library(linac MODULE  ${src_files})
python_extension_module(linac)
target_link_libraries(linac pyorbit)
install(TARGETS linac LIBRARY DESTINATION py/orbit/mod)
