## CMake notes
 - currently, and importantly, `from orbit.mod.bunch import Bunch;Bunch()` generates a segfault somehow. That makes this solution useless until resolved.
 - scikit-build required to build this, see also build dependencies in pyproject.toml
 - To compile, run `python setup.py bdist_wheel && pip install dist/orbit-*.whl`. Note that your python binary used here needs to be Python version 2 (and corresponding pip used).
 - src/files.cmake should contain list of all source files to build in the main pyorbit library.
 - To run after, you simply use the built in python interpreter (same you used to build with setup.py). E.g. go to the example folder and run `python lattice_test.py`. No environment configuration neeeded.
