#ifndef PIN_H
#define PIN_H

#include <inttypes.h>
#include <stdbool.h>

/*
 * A `pin_t` is an abstraction of a pin. When a pin_t variable is
 * declared you have to bind this variable with a physical pin to the
 * AVR microcontroler. This is done with pin_create(). With this
 * function is defined the direction of the pin also. It is possible
 * to read or write the pin value. pin_destroy() is used in order to
 * unbind the pin and leave it as in reset state.
 */

typedef enum {Input, Output} pin_direction_t;

typedef struct {
  volatile uint8_t *port;
  uint8_t pin;
} pin_t;

/* Allow general internal pull up */
void allow_in_up (bool p);

/* Create and bind the pin */
pin_t pin_create(volatile uint8_t *port, uint8_t pin, pin_direction_t d);

/* Write value `v` in pin `p` */
void pin_w(pin_t p, bool v);

/* Read and return value `v` in pin `p` */
bool pin_r(pin_t p);

/* Toggles value in pin `p` */
void pin_toggle(pin_t p);

/* Destroy and unbind the pin */
void pin_destroy(pin_t *const p);

#endif
