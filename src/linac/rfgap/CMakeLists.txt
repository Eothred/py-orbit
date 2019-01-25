file(GLOB src_files wrap_*.cc)
add_library(po_linac_rfgap ${src_files})
target_link_libraries(po_linac_rfgap pyorbit)
