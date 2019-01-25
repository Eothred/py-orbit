# Find all external projects we (optionally) need
# For optional, add option to turn on/off, default to on if 
# module is found
find_package (Python2 COMPONENTS Interpreter Development)
include_directories(${Python2_INCLUDE_DIR})
# FindPTC..

find_package(FFTW)

find_package(MPI)
include_directories(${MPI_INCLUDE_PATH})


# add all includes that subfolders may depend on:
include_directories(include)
include_directories(linac)
include_directories(mpi)
include_directories(orbit)
include_directories(orbit/Apertures)
include_directories(orbit/Errors)
include_directories(orbit/FieldTracker)
include_directories(orbit/Impedances)
include_directories(orbit/MaterialInteractions)
include_directories(orbit/RFCavities)
include_directories(orbit/ParticlesAttributes)
include_directories(orbit/BunchDiagnostics)
include_directories(spacecharge)
include_directories(teapot)
include_directories(trackerrk4)
include_directories(utils)
include_directories(utils/bunch)
include_directories(utils/integration)
include_directories(utils/matrix)
include_directories(utils/polynomial)


set(CMAKE_CXX_FLAGS "-fPIC")

# Install main library, excluding all wrap_ sources
include(files.cmake)
add_library(pyorbit ${pyorbit_src})
target_link_libraries(pyorbit ${FFTW_LIBRARIES} ${MPI_CXX_LIBRARIES})
install(TARGETS pyorbit
    LIBRARY DESTINATION lib
    COMPONENT Libraries
    ARCHIVE DESTINATION lib
    COMPONENT Libraries
)

# We add all subdirectories (that generate libraries)
add_subdirectory(linac)
add_subdirectory(mpi)
add_subdirectory(orbit)
add_subdirectory(spacecharge)
add_subdirectory(teapot)
add_subdirectory(trackerrk4)
add_subdirectory(utils)

## Finally we create the main project..
#add_executable(pyORBIT main/main)
#target_link_libraries(pyORBIT python2.7 po_linac po_mpi po_orbit po_spacecharge po_teapot po_trackerrk4 po_utils ${FFTW_LIBRARIES})
#python_standalone_executable(pyORBIT)

#add_subdirectory(tests)
