#include "hash_tables.h"

/**
 * hash_table_get - retrieves a value associated with a key
 * @ht: the table to look into
 * @key: the key with the value to retrieve
 * Return: the value associated with the key, or NULL if the key couldn't be found
 */
char *hash_table_get(const hash_table_t *ht, const char *key)
{
	unsigned long int idx;
	hash_node_t *temp;

	if (!ht || !ht->array || !ht->size || !key || strlen(key) == 0)
		return (NULL);
	idx = key_index((const unsigned char *)key, ht->size);
	temp = ht->array[idx];
	while (temp != NULL)
	{
		if (strcmp(temp->key, key) == 0)
			return (temp->value);
		temp = temp->next;
	}
	return (NULL);
}
