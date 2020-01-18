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
