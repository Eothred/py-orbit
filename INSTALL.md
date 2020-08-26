## CMake notes
 - scikit-build required to build this, see also build dependencies in pyproject.toml
 - To compile, run `python setup.py install`. Note that your python binary used here needs to be Python version 2. Note that if you do not have sudo rights you can add the argument `--user` to install. It will compile regardless but not work later on. So e.g. on my system I need to run `python2 setup.py install --user` since python points to python3 (and I do not have sudo rights).
 - src/files.cmake should contain list of all source files to build in the main pyorbit library.
 - To run after, you simply use the built in python interpreter (same you used to build with setup.py). E.g. go to the example folder and run `python lattice_test.py`. No environment configuration neeeded.
