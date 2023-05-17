#ifndef TIMER_H
#define TIMER_H

/*
 * This module implements a time dispatcher with a resolution
 * of 10 ms. It is based on callbacks. That is, functions which
 * are called after a specific (temporal) event ocurred.
 */

/* 
 * This timer has a maximum nomber of ticks of 2 bytes.
 * So a maximum of 655 seconds is possible if resolution is 10ms.
 * chrono is also extended.
 */


#define TIMER_MS(ms) (ms/5)
#define TIMER_ERR    -1

typedef void (*timer_callback_t)(void);
typedef int8_t timer_handler_t;
typedef int8_t timer_chrono_t;

void timer_init(void);
void timer_cancel_all(void);

timer_handler_t timer_ntimes(uint8_t n, uint16_t ticks, timer_callback_t f);
timer_handler_t timer_every(uint16_t ticks, timer_callback_t f);
timer_handler_t timer_after(uint16_t ticks, timer_callback_t f);
void timer_cancel(timer_handler_t h);

timer_chrono_t chrono(void);
void chrono_start(timer_chrono_t c);
uint16_t chrono_get(timer_chrono_t c);
void chrono_stop(timer_chrono_t c);
void chrono_cancel(timer_chrono_t c);

#endif
