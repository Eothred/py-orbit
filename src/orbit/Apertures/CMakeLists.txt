file(GLOB src_files *.cc)
add_library(po_orbit_apertures ${src_files})

# This is how the actual Python object should look like
add_library(aperture MODULE  ${src_files})
python_extension_module(aperture)
target_link_libraries(aperture po_orbit ${MPI_CXX_LIBRARIES})
install(TARGETS aperture LIBRARY DESTINATION .)
