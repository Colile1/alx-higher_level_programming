/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
listint_t *current = *head;
int stack[2048];
int top = 0, i = 0;
if (!current || !(current->next))
return (1);
while (current != NULL)
{
stack[top++] = current->n;
current = current->next;
}
current = *head;
while (current != NULL)
{
if (stack[--top] != current->n)
return (0);
current = current->next;
}
return (1);
}
