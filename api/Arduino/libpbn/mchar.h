#ifndef MCHAR_H
#define MCHAR_H

#include <inttypes.h>
#include <stdbool.h>

/*
 * This module define the mchar_t type which encodes
 * a char in morse code. It uses a byte packed coding.
 *   0 -> dot
 *   1 -> dash
 */

typedef enum {MDot, MDash} msign_t;

typedef uint8_t mchar_t;

typedef struct{
  mchar_t m;
  uint8_t mask,sentinel;
} mchar_iter_t;

/* number of signs of an mchar */
#define mchar_len(m) (uint8_t)(m & 0x7)

/*
 * This operation define mchar constants. Assume that
 * 0 -> dot; 1-> dash
 */
#define mchar(c) (mchar_t)((0b##c << (8-sizeof(#c)+1)) | (sizeof(#c)-1))

/* empty mchar: it's no a proper mchar */
#define mchar_empty (mchar_t)0

/* adds a new sign to an mchar */
mchar_t mchar_add(mchar_t m, msign_t s);

/* mchar iterator */
mchar_iter_t mchar_iter(mchar_t m);
msign_t mchar_next(mchar_iter_t *const i);
bool mchar_valid(mchar_iter_t i); 

#endif
