file(GLOB src_files *.cc)
add_library(po_trackerrk4 ${src_files})


install(TARGETS po_trackerrk4
    LIBRARY DESTINATION lib
    COMPONENT Libraries
    ARCHIVE DESTINATION lib
    COMPONENT Libraries
)
