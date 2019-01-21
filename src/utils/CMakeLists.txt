include_directories(statistics)

add_subdirectory(bunch)
add_subdirectory(integration)
add_subdirectory(matrix)
add_subdirectory(polynomial)
add_subdirectory(statistics)

file(GLOB src_files *.cc)
add_library(po_utils ${src_files})

target_link_libraries(po_utils po_utils_bunch po_utils_integration po_utils_matrix po_utils_polynomial po_utils_statistics )

install(TARGETS po_utils po_utils_bunch po_utils_integration po_utils_matrix po_utils_polynomial po_utils_statistics
    LIBRARY DESTINATION lib
    COMPONENT Libraries
    ARCHIVE DESTINATION lib
    COMPONENT Libraries
)
