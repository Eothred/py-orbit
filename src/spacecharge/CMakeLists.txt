file(GLOB sc_src_files *.cc)
add_library(po_spacecharge ${sc_src_files})
target_link_libraries(po_spacecharge ${FFTW_LIBRARIES} ${MPI_CXX_LIBRARIES})

install(TARGETS po_spacecharge
    LIBRARY DESTINATION lib
    COMPONENT Libraries
    ARCHIVE DESTINATION lib
    COMPONENT Libraries
)

add_library(spacecharge MODULE wrap_spacecharge)
python_extension_module(spacecharge)
target_link_libraries(spacecharge po_spacecharge)
install(TARGETS spacecharge LIBRARY DESTINATION .)
