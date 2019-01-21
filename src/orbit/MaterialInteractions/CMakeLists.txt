file(GLOB src_files *.cc)
add_library(po_orbit_materialint ${src_files})
target_link_libraries(po_orbit_materialint po_utils)
