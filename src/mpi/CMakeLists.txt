file(GLOB src_files *.cc)
add_library(po_mpi ${src_files})


install(TARGETS po_mpi
    LIBRARY DESTINATION lib
    COMPONENT Libraries
    ARCHIVE DESTINATION lib
    COMPONENT Libraries
)
