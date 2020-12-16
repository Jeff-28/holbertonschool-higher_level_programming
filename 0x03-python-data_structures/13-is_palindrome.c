#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: the start of the list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head);
{
	int len = 0, i = 0;
	int list[];

	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	while (*head != NULL)
	{
		len++;
		list[len - 1] = (*head)->n;
		head = &(*head)->next;
	}
	while (i < len / 2)
	{
		if (list[i] != list[len - i - 1])
		{
			return (0);
		}
		i++;
	}
	return (1);
}
