from skbuild import setup

setup(
    name = "orbit",
    version = "1.0",
    description = "Particle Tracking Code",
    url = "https://pyorbit-collaboration.github.io/",
    packages = ["spam", "orbit", "orbit.utils", "orbit.mpi"],
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
    cmake_args = ['-DBUILD_SHARED_LIBS:BOOL=ON']
    )
