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
add_library(_mpi MODULE  ${src_files})
python_extension_module(_mpi)
target_link_libraries(_mpi ${MPI_CXX_LIBRARIES})
install(TARGETS _mpi LIBRARY DESTINATION orbit/mpi)
