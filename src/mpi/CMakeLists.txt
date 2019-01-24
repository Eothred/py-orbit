file(GLOB src_files *.cc)
add_library(po_mpi ${src_files})
target_link_libraries(po_mpi ${MPI_CXX_LIBRARIES})

install(TARGETS po_mpi
    LIBRARY DESTINATION lib
    COMPONENT Libraries
    ARCHIVE DESTINATION lib
    COMPONENT Libraries
)
