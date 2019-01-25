file(GLOB src_files *.cc)
add_library(po_mpi ${src_files})
target_link_libraries(po_mpi ${MPI_CXX_LIBRARIES})

install(TARGETS po_mpi
    LIBRARY DESTINATION lib
    COMPONENT Libraries
    ARCHIVE DESTINATION lib
    COMPONENT Libraries
)

# This is how the actual Python object should look like
add_library(orbit_mpi MODULE  ${src_files})
python_extension_module(orbit_mpi)
target_link_libraries(orbit_mpi po_orbit ${MPI_CXX_LIBRARIES})
install(TARGETS orbit_mpi LIBRARY DESTINATION .)
