#ifndef LAMP_H
#define LAMP_H
#include "pin.h"
#include <stdint.h>
#include <stdbool.h>

/*Definim els tres colors possibles del semafor*/
typedef enum{Green, Yellow, Red} color_t;

/*Agrupacio de LEDS amb els tres colors*/
typedef struct{
  pin_t green;
  pin_t yellow;
  pin_t red;
}lamp_t;

/*Fa un bind entre el tipus lamp_t i cadascun dels 3 pins fisics.
 S'inicialitza amb tots els LEDS apagats*/
void lamp_init(lamp_t *const l, 
	       volatile uint8_t *prtg, uint8_t pg,
	       volatile uint8_t *prty, uint8_t py,
	       volatile uint8_t *prtr, uint8_t pr);

/*Encen el LED de color c de la lampada l*/
void lamp_on(lamp_t l, color_t c);

/*Apaga el LED de color c de la lampada l*/
void lamp_off(lamp_t l, color_t c);

/*Commuta l'estat del color c en la lampada l*/
void lamp_toggle(lamp_t l, color_t c);

/*Retorna true si en la lampada l el color c esta ences*/
bool lamp_is_on(lamp_t l, color_t c);

#endif
