#ifndef QUEUE_H
#define QUEUE_H

#include <inttypes.h>
#include <stdbool.h>

#define QL (1<<7)

typedef struct {
  uint8_t t[QL];
  uint8_t front, rear;
} queue_t;


/*
 * Intializes `q` to empty. This function don't guarantees
 * mutual exclusion.
 */
void queue_empty(queue_t *const q);

/* Returns true iff `q` is empty */
bool queue_is_empty(const queue_t *const q);

/* Return true iff `q` is full */
bool queue_is_full(const queue_t *const q);

/* Adds `v` to `q`. If `q` is full nothing is added */
void queue_enqueue(queue_t *const q, uint8_t v);

/* 
 * Remove the front element of `q`. If `q` is empty nothing is
 * removed.
 */
void queue_dequeue(queue_t *const q);

/* 
 * Return the front of `q`. If `q` is empty an undefined value
 * is returned.
 */
uint8_t queue_front(const queue_t *const q);


#endif
