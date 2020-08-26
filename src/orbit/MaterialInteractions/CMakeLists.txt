include_directories(${CMAKE_CURRENT_SOURCE_DIR})

add_library(foil MODULE  wrap_foil.cc)
python_extension_module(foil)
target_link_libraries(foil pyorbit)
install(TARGETS foil LIBRARY DESTINATION py/orbit/mod)

add_library(collimator MODULE  wrap_collimator.cc)
python_extension_module(collimator)
target_link_libraries(collimator pyorbit)
install(TARGETS collimator LIBRARY DESTINATION py/orbit/mod)
