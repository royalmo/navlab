#ifndef ETHER_TX_H
#define ETHER_TX_H

/* New structure project for module ether.
   A ether_definitions.h common to ether_tx and ether_rx modules.
   A ether module composed by ether_tx and ether_rx modules.
   
   Started 13-11-2020
*/

#include <stdbool.h>
#include "ether_definitions.h"

void init_transmitter(void);
void ether_put(morse_c_t c);
bool is_transmitting(void);
void on_finish_tx(ether_cll_t ftx);

#endif /* ETHER_TX_H */
