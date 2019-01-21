file(GLOB src_files *.cc)
add_library(po_teapot ${src_files})


install(TARGETS po_teapot
    LIBRARY DESTINATION lib
    COMPONENT Libraries
    ARCHIVE DESTINATION lib
    COMPONENT Libraries
)
