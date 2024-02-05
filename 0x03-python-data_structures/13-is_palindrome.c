#INCLUDE "LISTS.H"

/**
 * reverse_listint - reverses the order of nodes in a linked list
 * @pnt_hd: pointer to the first node in the list
 *
 * Return: pointer to the first node in the reversed list
 */
void reverse_listint(listint_t **pnt_hd)
{
listint_t *prev = NULL;
listint_t *current = *pnt_hd;
listint_t *next = NULL;

while (current)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*pnt_hd = prev;
}

/**
 * is_palindrome - checks if nodes in a linked list are equal when traversed in reverse
 * @pnt_hd: double pointer to the linked list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **pnt_hd)
{
listint_t *slow = *pnt_hd, *fast = *pnt_hd, *temp = *pnt_hd, *dup = NULL;

if (*pnt_hd == NULL || (*pnt_hd)->next == NULL)
return (1);

while (1)
{
fast = fast->next->next;
if (!fast)
{
dup = slow->next;
break;
}
if (!fast->next)
{
dup = slow->next->next;
break;
}
slow = slow->next;
}

reverse_listint(&dup);

while (dup && temp)
{
if (temp->n == dup->n)
{
dup = dup->next;
temp = temp->next;
}
else
return (0);
}

if (!dup)
return (1);

return (0);
}
