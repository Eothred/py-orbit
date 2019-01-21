include_directories(${CMAKE_CURRENT_SOURCE_DIR})

add_subdirectory(rfgap)
add_subdirectory(tracking)

include_directories(rfgap)
include_directories(tracking)

file(GLOB src_files *.cc)
add_library(po_linac ${src_files})

target_link_libraries(po_linac po_linac_rfgap po_linac_tracking)

install(TARGETS po_linac po_linac_rfgap po_linac_tracking
    LIBRARY DESTINATION lib
    COMPONENT Libraries
    ARCHIVE DESTINATION lib
    COMPONENT Libraries
)
