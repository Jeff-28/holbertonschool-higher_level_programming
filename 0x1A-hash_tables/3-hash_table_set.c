#include "hash_tables.h"
/**
 * create_node - creates a new node
 * @key: is the key, cannot be empty string
 * @value: value associated with the key, must be duplicated
 * Return: pointer to the new node, or NULL on failure
 */
hash_node_t *create_node(const char *key, const char *value)
{
	hash_node_t *node;

	node = malloc(sizeof(hash_node_t));
	if (!node)
		return (NULL);
	node->key = strdup(key);
	if (!node->key)
	{
		free(node);
		return (NULL);
	}
	node->value = strdup(value);
	if (!node->value)
	{
		free(node->key);
		free(node);
		return (NULL);
	}
	node->next = NULL;
	return (node);
}
/**
 * hash_table_set - adds an element to the hash table
 * @ht: the hash table to add or update the key/value
 * @key: is the key, cannot be empty string
 * @value: the value associated with the key, value must be duplicated
 * Return: 1 if it succeeded, 0 otherwise
 */
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	unsigned long int idx;
	hash_node_t *temp, *node;
	char *new_val;

	if (!ht || !ht->array || !ht->size || !key || strlen(key) == 0 || !value)
		return (0);
	idx = key_index((const unsigned char *)key, ht->size);
	temp = ht->array[idx];

	while (temp != NULL)
	{
		if (strcmp(temp->key, key) == 0)
		{
			new_val = strdup(value);
			if (!new_val)
				return (0);
			free(temp->value);
			temp->value = new_val;
			return (1);
		}
		temp = temp->next;
	}
	node = create_node(key, value);
	if (!node)
		return (0);
	node->next = ht->array[idx];
	ht->array[idx] = node;
	return (1);
}
