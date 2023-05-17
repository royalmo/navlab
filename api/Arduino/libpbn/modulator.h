#ifndef MODULATOR_H
#define MODULATOR_H

#include <stdbool.h>
/*
 * The module implements a trivial modulator that
 * outputs the signat through fixed pin PB3.
 * This means that TMR2 is use as a resource.
 * A no modulated signal is output by PCB LED pin PB5.
 */

/*
 * Initializes the module. 
 */

void modulator_init(void);

/* 
 * true means high level 
 */
void modulator_set(bool l);

#endif
