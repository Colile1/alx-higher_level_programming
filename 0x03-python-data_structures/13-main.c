#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
listint_t *pnt_hd;

pnt_hd = NULL;
add_nodeint_end(&pnt_hd, 1);
add_nodeint_end(&pnt_hd, 17);
add_nodeint_end(&pnt_hd, 972);
add_nodeint_end(&pnt_hd, 50);
add_nodeint_end(&pnt_hd, 98);
add_nodeint_end(&pnt_hd, 98);
add_nodeint_end(&pnt_hd, 50);
add_nodeint_end(&pnt_hd, 972);
add_nodeint_end(&pnt_hd, 17);
add_nodeint_end(&pnt_hd, 1);
print_listint(pnt_hd);

if (is_palindrome(&pnt_hd) == 1)
printf("Linked list is a palindrome\n");
else
printf("Linked list is not a palindrome\n");

free_listint(pnt_hd);

return (0);
}
