#include "Python.h"
#include "orbit_mpi.hh"

#include <iostream>

//modules headers
#include "wrap_orbit_mpi.hh"

/**
 * The main function that will initialize the MPI and will
 * call the python interpreter: Py_Main(argc,argv).
 */

int main(int argc, char **argv)
{

  ORBIT_MPI_Init(&argc, &argv);

  // We need to initialize the extra ORBIT MPI module
  Py_Initialize();

  // ORBIT mpi module initialization
  wrap_orbit_mpi::initorbit_mpi();

  // The python interpreter
  // It will call Py_Initialize() again, but there is no harm.
  Py_Main(argc, argv);

  ORBIT_MPI_Finalize();

  return 0;
}
