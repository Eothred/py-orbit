file(GLOB src_files *.cc)
add_library(po_teapot ${src_files})


install(TARGETS po_teapot
    LIBRARY DESTINATION lib
    COMPONENT Libraries
    ARCHIVE DESTINATION lib
    COMPONENT Libraries
)

# This is how the actual Python object should look like
add_library(teapot_base MODULE  wrap_teapotbase)
python_extension_module(teapot_base)
# I think this needs spacecharge as well?
target_link_libraries(teapot_base po_teapot pyorbit)
install(TARGETS teapot_base LIBRARY DESTINATION .)
