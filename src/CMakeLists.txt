# Find all external projects we (optionally) need
# For optional, add option to turn on/off, default to on if 
# module is found
find_package (Python2 COMPONENTS Interpreter Development)
include_directories(${Python2_INCLUDE_DIR})
# FindPTC..

find_package(FFTW)

# add all includes that subfolders may depend on:
include_directories(main)
include_directories(mpi)
include_directories(orbit)
include_directories(orbit/ParticlesAttributes)
include_directories(orbit/BunchDiagnostics)
include_directories(spacecharge)
include_directories(utils)
include_directories(utils/bunch)
include_directories(utils/integration)
include_directories(utils/matrix)
include_directories(utils/polynomial)

# We add all subdirectories (that generate libraries)
add_subdirectory(linac)
add_subdirectory(mpi)
add_subdirectory(orbit)
add_subdirectory(spacecharge)
add_subdirectory(teapot)
add_subdirectory(trackerrk4)
add_subdirectory(utils)

# Now all the additional folders main takes headers from:
include_directories(linac)
include_directories(teapot)
include_directories(orbit/Apertures)
include_directories(orbit/Errors)
include_directories(orbit/FieldTracker)
include_directories(orbit/Impedances)
include_directories(orbit/MaterialInteractions)
include_directories(orbit/RFCavities)
include_directories(teapot)
include_directories(trackerrk4)

# Finally we create the main project..
add_executable(pyORBIT main/main)
target_link_libraries(pyORBIT python2.7 po_linac po_mpi po_orbit po_spacecharge po_teapot po_trackerrk4 po_utils ${FFTW_LIBRARIES})

install(TARGETS pyORBIT
    RUNTIME DESTINATION bin
)
