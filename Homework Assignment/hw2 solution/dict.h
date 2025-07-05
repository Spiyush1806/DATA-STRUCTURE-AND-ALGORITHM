#ifndef DICT_H
#define DICT_H

#include "dict_adt.h"

typedef struct trie_node {
    struct trie_node *children[26]; // 26 lowercase English letters
    int value; // value associated with the key
    int is_end_of_key; // 1 if this node marks the end of a key, 0 otherwise
} trie_node;

typedef struct trie {
    trie_node *root;
} trie;

#endif