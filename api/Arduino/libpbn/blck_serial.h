#ifndef BLCKSERIAL_H
#define BLCKSERIAL_H

#include <stdint.h>

/* readbclk(char s[])
 * Read a block until a non printable character is found.
 * Returns the length.
 */

void print(char s[]);
uint8_t readblck(char s[]);

#endif
