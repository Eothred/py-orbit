from skbuild import setup

setup(
    name = "orbit",
    version = "1.0",
    description = "Particle Tracking Code",
    url = "https://pyorbit-collaboration.github.io/",
    package_dir = { '': 'py' },
    packages = ['orbit',
                'orbit.aperture',
                'orbit.bumps',
                'orbit.bunch_generators',
                'orbit.bunch_utils',
                'orbit.collimation',
                'orbit.diagnostics',
                'orbit.errors',
                'orbit.fieldtracker',
                'orbit.foils',
                'orbit.impedances',
                'orbit.injection',
                'orbit.kickernodes',
                'orbit.lattice',
                'orbit.matching',
                'orbit.matrix_lattice',
                'orbit.orbit_correction',
                'orbit.parsers',
                'orbit.py_linac',
                'orbit.py_linac.lattice',
                'orbit.py_linac.lattice_modifications',
                'orbit.py_linac.linac_parsers',
                'orbit.py_linac.overlapping_fields',
                'orbit.py_linac.rf_field_readers',
                'orbit.rf_cavities',
                'orbit.sns_linac',
                'orbit.space_charge',
                'orbit.space_charge.directforce2p5d',
                'orbit.space_charge.sc1d',
                'orbit.space_charge.sc2dslicebyslice',
                'orbit.space_charge.sc2p5d',
                'orbit.space_charge.sc3d',
                'orbit.teapot',
                'orbit.teapot_base',
                'orbit.time_dep',
                'orbit.utils',
                'orbit.utils.fitting',
                'orbit.utils.xml',
                'orbit.utils.orbit_mpi_utils',
               ],
    scripts = ['bin/pyORBIT'],
    classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 4 - Beta',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    ],
    cmake_args = ['-DBUILD_SHARED_LIBS:BOOL=ON', '-DUSE_MPI=OFF']
    )
