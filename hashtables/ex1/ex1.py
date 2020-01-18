#  Hint:  You may not need all of these.
# Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)
    
    for index, w in enumerate(weights):
        hash_table_insert(ht, w, index)

    for index_1, w_1 in enumerate(weights):
        w_2 = limit - w_1
        index_2 = hash_table_retrieve(ht, w_2)

        if index_2:
            if index_1 > index_2:
                return (index_1, index_2)
            else:
                return (index_2, index_1)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
