include_directories(SynchPartRedefinition)

add_subdirectory(Apertures)
add_subdirectory(BunchDiagnostics)
add_subdirectory(Errors)
add_subdirectory(FieldTracker)
add_subdirectory(Impedances)
add_subdirectory(MaterialInteractions)
add_subdirectory(ParticlesAttributes)
add_subdirectory(RFCavities)
add_subdirectory(SynchPartRedefinition)


file(GLOB src_files *.cc)
add_library(po_orbit ${src_files})

target_link_libraries(po_orbit po_orbit_apertures po_orbit_bunchdiag po_orbit_errors po_orbit_fieldtracker po_orbit_impedances po_orbit_materialint po_orbit_pattr po_orbit_rfcav po_orbit_synchpartredef)

install(TARGETS po_orbit po_orbit_apertures po_orbit_bunchdiag po_orbit_errors po_orbit_fieldtracker po_orbit_impedances po_orbit_materialint po_orbit_pattr po_orbit_rfcav po_orbit_synchpartredef
    LIBRARY DESTINATION lib
    COMPONENT Libraries
    ARCHIVE DESTINATION lib
    COMPONENT Libraries
)
