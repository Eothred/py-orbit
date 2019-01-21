file(GLOB sc_src_files *.cc)
add_library(po_spacecharge ${sc_src_files})


install(TARGETS po_spacecharge
    LIBRARY DESTINATION lib
    COMPONENT Libraries
    ARCHIVE DESTINATION lib
    COMPONENT Libraries
)
