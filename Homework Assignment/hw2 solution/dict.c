#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "dict.h"

// Create an empty Dict
Dict make_dict() {
    trie *dict = (trie *) malloc(sizeof(trie));
    if (dict == NULL) {
        return NULL;
    }
    dict->root = (trie_node *) malloc(sizeof(trie_node));
    if (dict->root == NULL) {
        free(dict);
        return NULL;
    }
    for (int i = 0; i < 26; i++) {
        dict->root->children[i] = NULL;
    }
    dict->root->value = 0;
    dict->root->is_end_of_key = 0;
    return (Dict) dict;
}

// Free up all memory allocated to a Dict
void free_dict(Dict dict_adt) {
    if (dict_adt != NULL) {
        trie *dict = (trie *) dict_adt;
        free_trie_node(dict->root);
        free(dict);
    }
}

// Helper function to free a trie node and its children
void free_trie_node(trie_node *node) {
    if (node != NULL) {
        for (int i = 0; i < 26; i++) {
            if (node->children[i] != NULL) {
                free_trie_node(node->children[i]);
            }
        }
        free(node);
    }
}

// Get a pointer to the value associated with key
int *get(Dict dict_adt, const char *key) {
    if (dict_adt == NULL) {
        return NULL;
    }
    trie *dict = (trie *) dict_adt;
    trie_node *current = dict->root;
    for (int i = 0; i < strlen(key); i++) {
        int index = key[i] - 'a';
        if (current->children[index] == NULL) {
            return NULL;
        }
        current = current->children[index];
    }
    if (current->is_end_of_key == 1) {
        return &current->value;
    } else {
        return NULL;
    }
}

// Set the value associated with key to value
int set(Dict dict_adt, const char *key, int value) {
    if (dict_adt == NULL) {
        return 0;
    }
    trie *dict = (trie *) dict_adt;
    trie_node *current = dict->root;
    for (int i = 0; i < strlen(key); i++) {
        int index = key[i] - 'a';
        if (current->children[index] == NULL) {
            current->children[index] = (trie_node *) malloc(sizeof(trie_node));
            if (current->children[index] == NULL) {
                return 0; // out of memory
            }
            for (int j = 0; j < 26; j++) {
                current->children[index]->children[j] = NULL;
            }
            current->children[index]->value = 0;
            current->children[index]->is_end_of_key = 0;
        }
        current = current->children[index];
    }
    current->value = value;
    current->is_end_of_key = 1;
    return 1;
}

// Print the contents of the dictionary
void print_dict(Dict dict_adt) {
    if (dict_adt == NULL) {
        return;
    }
    trie *dict = (trie *) dict_adt;
    print_trie_node(dict->root, "");
}

// Helper function to print a trie node and its children
void print_trie_node(trie_node *node, char *prefix) {
    if (node != NULL) {
        if (node->is_end_of_key == 1) {
            printf("%s: %d\n", prefix, node->value);
        }
        for (int i = 0; i < 26; i++) {
            if (node->children[i] != NULL) {
                char new_prefix[strlen(prefix) + 2];
                strcpy(new_prefix, prefix);
                new_prefix[strlen(prefix)] = 'a' + i;
                new_prefix[strlen(prefix) + 1] = '\0';
                print_trie_node(node->children[i], new_prefix);
            }
        }
    }
}