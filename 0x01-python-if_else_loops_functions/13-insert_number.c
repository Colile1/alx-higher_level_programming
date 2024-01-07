#include "lists.h"

/**
 * insert_node - Iadds a number into a sorted singly-linked list.
 * @pnt_hd: Pointer to the pnt_hd of the linked list.
 * @number: The number to insert.
 * Author - Tolulope Fakunle
 * Return: NULL if function fails, else 
 *         return a pointer to the new node.
 */
listint_t *insert_node(listint_t **pnt_hd, int number)
{
	listint_t *node = *pnt_hd, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*pnt_hd = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
