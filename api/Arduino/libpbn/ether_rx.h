#ifndef ETHER_RX_H
#define ETHER_RX_H

/* Receiver module 
 * Started: 14-11-20
 * DEM Morse
 * This module use modulator module for MODULATOR
 * and implements a DEModulator on PORTD pin2 by 
 * interrupt INT0
 */

#include <stdbool.h>
#include "ether_definitions.h"

void init_receiver(eth_mode_t m);
void enable_receiver(bool active);
bool ether_can_get(void);
morse_c_t ether_get(void);
bool is_receiving(void);
void on_start_receiving(ether_cll_t s);
void on_finish_receiving(ether_cll_t f);

#endif /* ETHER_RX_H */
