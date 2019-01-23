#ifndef WRAP_SPACE_CHARGE_H
#define WRAP_SPACE_CHARGE_H

#include "Python.h"

#ifdef __cplusplus
extern "C" {
#endif

  namespace wrap_spacecharge
  {
	void initspacecharge(void);
	PyObject* getSpaceChargeType(const char* name);
  }
	
#ifdef __cplusplus
}
#endif  // __cplusplus

#endif // WRAP_SPACE_CHARGE_H
