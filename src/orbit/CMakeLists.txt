include_directories(SynchPartRedefinition)

add_subdirectory(Apertures)

add_library(bunch MODULE wrap_bunch)
python_extension_module(bunch)
target_link_libraries(bunch pyorbit ${FFTW_LIBRARIES} ${MPI_CXX_LIBRARIES})
install(TARGETS bunch LIBRARY DESTINATION .)
