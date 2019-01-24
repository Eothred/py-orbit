file(GLOB src_files *.cc)
add_library(po_utils_bunch ${src_files})
target_link_libraries(po_utils_bunch po_orbit_pattr)
