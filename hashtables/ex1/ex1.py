#  Hint:  You may not need all of these.
# Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)
    # TODO: YOUR CODE HERE
    for index, w in enumerate(weights):
        hash_table_insert(ht, w, index)
    for pair in ht.storage:
        while pair:
            s_key = limit - pair.key
            if s_key in weights:
                s_index = hash_table_retrieve(ht, s_key)
                if pair.key < s_key:
                    return (s_index, pair.value)
                elif pair.key > s_key:
                    return (pair.value, s_index)
                else:
                    return (1, 0)
            pair = pair.next

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
