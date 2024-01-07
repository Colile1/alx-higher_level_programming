#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer number
 * @next: pointer to next node
 * 
 * Description: structure of a singly linked list node
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **pnt_hd, const int n);
void free_listint(listint_t *pnt_hd);
listint_t *insert_node(listint_t **pnt_hd, int number);

#endif
