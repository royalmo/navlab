/* New structure project for module ether.
   A ether_definitions.h common to ether_tx and ether_rx modules.
   A ether module composed by ether_tx and ether_rx modules.
   
   Started 13-11-2020
*/


#ifndef ETHER_DEFINITIONS_H
#define ETHER_DEFINITIONS_H

#include <stdint.h>

/* Sign durations in ticks */
#define DOT TIMER_MS(80)
#define DASH (DOT*3)
#define GAP DOT
#define CHARGAP DASH
#define LONGGAP (DOT*7)

typedef uint8_t morse_c_t; //Only A..Z and 0..9 valid
typedef void (*ether_cll_t)(void); //Callback functions
typedef enum {Normal, InvertedRX} eth_mode_t; //Configuration modes of Ether layer
/* InvertedRX: Reception is inverted polarity
 */


#endif /* ETHER_DEFINITIONS_H */
