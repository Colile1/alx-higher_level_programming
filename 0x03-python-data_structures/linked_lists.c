#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to pnt_hd of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
const listint_t *current;
unsigned int n;

current = h;
n = 0;
while (current != NULL)
{
printf("%i\n", current->n);
current = current->next;
n++;
}

return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @pnt_hd: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **pnt_hd, const int n)
{
listint_t *new;
listint_t *current;

current = *pnt_hd;

new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);

new->n = n;
new->next = NULL;

if (*pnt_hd == NULL)
*pnt_hd = new;
else
{
while (current->next != NULL)
current = current->next;
current->next = new;
}

return (new);
}

/**
 * free_listint - frees a listint_t list
 * @pnt_hd: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *pnt_hd)
{
listint_t *current;

while (pnt_hd != NULL)
{
current = pnt_hd;
pnt_hd = pnt_hd->next;
free(current);
}
}
