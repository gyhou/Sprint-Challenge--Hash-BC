#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    for t in tickets:
        hash_table_insert(ht, t.source, t.destination)

    index = 0
    destination = hash_table_retrieve(ht, "NONE")
    while index < length:
        route[index] = destination
        destination = hash_table_retrieve(ht, destination)
        index += 1

    return route

    # for i in range(length):
    #     if tickets[i].source == "NONE":
    #         route[0] = tickets[i].destination
    #     hash_table_insert(ht, tickets[i].source, tickets[i].destination)

    # for j in range(length):
    #     if route[j-1] is not None:
    #         route[j] = hash_table_retrieve(ht, route[j-1])

    # return route
