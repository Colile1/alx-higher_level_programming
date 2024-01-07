#include "lists.h"

/**
 * print_listint - Prints all elements of a listint_t list
 * @h: A pointer to the head of the listint_t list
 *
 * Return: The number of nodes in the listint_t list
 */
size_t print_listint(const listint_t *h)
{
const listint_t *current = h;
size_t count = 0;

while (current != NULL)
{
printf("%d\n", current->n);
current = current->next;
count++;
}
return count;
}

/**
 * add_nodeint_end - Adds a new node at the end of a listint_t list
 * @head: A pointer to the pointer of the head of the listint_t list
 * @n: The integer for the new node to contain
 *
 * Return: If the function fails - NULL.
 * Otherwise - the address of the new element
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
listint_t *new_node = malloc(sizeof(listint_t));
listint_t *temp;

if (new_node == NULL)
return (NULL);

new_node->n = n;
new_node->next = NULL;

if (*head == NULL)
{
*head = new_node;
}
else
{
temp = *head;
while (temp->next != NULL)
temp = temp->next;

temp->next = new_node;
}
return (new_node);
}

/**
 * free_listint - Frees a listint_t list
 * @head: A pointer to the head of the listint_t list to free
 *
 * Return: void
 */
void free_listint(listint_t *head)
{
listint_t *temp;

while (head != NULL)
{
temp = head;
head = head->next;
free(temp);
}
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: A pointer to the head of the linked list
 *
 * Return: If the linked list is not a palindrome - 0.
 * If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
listint_t *fast = *head;
listint_t *slow = *head;
listint_t *prev_slow = NULL;
listint_t *midnode = NULL;
listint_t *second_half;
int result = 1;

if (*head != NULL && (*head)->next != NULL)
{
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev_slow = slow;
slow = slow->next;
}

if (fast != NULL)
{
midnode = slow;
slow = slow->next;
}

second_half = slow;
prev_slow->next = NULL;
reverse_listint(&second_half);

result = compare_lists(*head, second_half);

reverse_listint(&second_half);
y
if (midnode != NULL)
{
prev_slow->next = midnode;
midnode->next = second_half;
}
else
{
prev_slow->next = second_half;
}
}
return result;
}

/**
 * reverse_listint - Reverses a listint_t linked list
 * @head: A pointer to the head of the listint_t list
 *
 * Return: void
 */
void reverse_listint(listint_t **head)
{
listint_t *current = *head;
listint_t *next = NULL;
listint_t *prev = NULL;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
*head = prev;
}
