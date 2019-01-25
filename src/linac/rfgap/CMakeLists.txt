file(GLOB src_files *.cc)
add_library(po_linac_rfgap ${src_files})
target_link_libraries(po_linac_rfgap po_orbit)
