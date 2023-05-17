#ifndef BLK_ETHER_H
#define BLK_ETHER_H

#include <inttypes.h>
#include <stdbool.h>

#include "ether_definitions.h"

/*
 * MO-DEM Morse
 * This module use modulator module for MODULATOR
 * and implements a DEModulator on PORTD pin2 by 
 * interrupt INT0
 */

void ether_init(eth_mode_t mod);

#define MAX_ME_ETH 126    //Depending on QL in queue module (1 position to empty/full)

//nova API
typedef morse_c_t missatge_eth_t[MAX_ME_ETH];

bool ether_busy(void);
// true if ether is transmitting or receiving

bool ether_can_put(void);
// true if ether_block_put() can be called

void ether_block_put(missatge_eth_t m);
// Can be called if !ether_busy()

void ether_block_get(missatge_eth_t m);
// Can be called only after a on_message_received event

void on_message_received(ether_cll_t m);
void on_finish_transmission(ether_cll_t f);

#endif
