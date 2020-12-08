#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the list to check.
 * Return: 1 if it has a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
