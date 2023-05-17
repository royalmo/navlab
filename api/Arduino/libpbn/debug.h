#ifndef DEBUG_H
#define DEBUG_H

/* Header for TRACE() definition
   Need:
     include "serial.h"
     serial_open()
   Define DEBUG_MODE in CPPFLAGS to enable Debug
   INIT_TRACE to initialize
*/

#include "serial.h"

#ifdef DEBUG_MODE
  #define TRACE(x) serial_put(x)
  #define TRACE_STR(x) print(x)
  #define INIT_TRACE serial_open()
#else
  #define TRACE(x)
  #define TRACE_STR(x)
  #define INIT_TRACE
#endif // DEBUG_MODE

#endif /* DEBUG_H */
