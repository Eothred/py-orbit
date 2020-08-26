# Find all external projects we (optionally) need
# For optional, add option to turn on/off, default to on if 
# module is found
find_package (Python2 REQUIRED COMPONENTS Interpreter Development)
include_directories(${Python2_INCLUDE_DIRS})
# FindPTC..

find_package(FFTW)

find_package(MPI)
include(CMakeDependentOption)
CMAKE_DEPENDENT_OPTION(USE_MPI "Enable MPI capabilities" ON "MPI_FOUND" OFF)
if(USE_MPI)
    add_definitions("-DUSE_MPI")
    include_directories(${MPI_INCLUDE_PATH})
endif(USE_MPI)


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
include_directories(orbit/SynchPartRedefinition)
include_directories(spacecharge)
include_directories(teapot)
include_directories(trackerrk4)
include_directories(utils)
include_directories(utils/bunch)
include_directories(utils/harmonic_analysis)
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
    ARCHIVE DESTINATION lib
    COMPONENT Libraries
)

# We add all subdirectories (that generate libraries)
add_subdirectory(linac)
add_subdirectory(mpi)
add_subdirectory(orbit)
add_subdirectory(spacecharge)
add_subdirectory(teapot)
add_subdirectory(utils)

# Finally we create the main project..
include_directories(linac/rfgap)
include_directories(linac/tracking)
include_directories(utils/statistics)
add_executable(pyORBIT main/main ${all_wrap_src})
target_link_libraries(pyORBIT python2.7 pyorbit ${FFTW_LIBRARIES})
#python_standalone_executable(pyORBIT)
install(TARGETS pyORBIT
    RUNTIME DESTINATION bin
)

#add_subdirectory(tests)
