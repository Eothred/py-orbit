file(GLOB src_files *.cc)
add_library(po_linac_tracking ${src_files})
target_link_libraries(po_linac_tracking po_orbit ${MPI_CXX_LIBRARIES})

# This is how the actual Python object should look like
add_library(linac_tracking MODULE wrap_linac_tracking)
python_extension_module(linac_tracking)
target_link_libraries(linac_tracking po_linac_tracking)
install(TARGETS linac_tracking LIBRARY DESTINATION .)
