include_directories(statistics)

add_subdirectory(bunch)
add_subdirectory(integration)
add_subdirectory(matrix)
add_subdirectory(polynomial)
add_subdirectory(statistics)

file(GLOB src_files *.cc)
add_library(po_utils ${src_files})

target_link_libraries(po_utils po_utils_bunch po_utils_integration po_utils_matrix po_utils_polynomial po_utils_statistics po_mpi)

install(TARGETS po_utils po_utils_bunch po_utils_integration po_utils_matrix po_utils_polynomial po_utils_statistics
    LIBRARY DESTINATION lib
    COMPONENT Libraries
    ARCHIVE DESTINATION lib
    COMPONENT Libraries
)



# This is how the actual Python object should look like
add_library(orbit_utils MODULE  ${src_files})
python_extension_module(orbit_utils)
target_link_libraries(orbit_utils pyorbit po_utils_bunch po_utils_integration po_utils_matrix po_utils_polynomial po_utils_statistics po_mpi)
#target_link_libraries_with_dynamic_lookup(_utils po_utils_bunch po_utils_integration po_utils_matrix po_utils_polynomial po_utils_statistics po_mpi)
install(TARGETS orbit_utils LIBRARY DESTINATION .)
