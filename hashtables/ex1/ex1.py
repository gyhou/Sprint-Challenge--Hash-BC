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
        if pair:
            second_key = limit - pair.key
            if second_key in weights:
                second_index = hash_table_retrieve(ht, second_key)
                if second_index != pair.value:
                    if pair.key <= second_key:
                        return (second_index, pair.value)
                    else:
                        return (pair.value, second_index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
