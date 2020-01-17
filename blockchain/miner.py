import hashlib
import requests

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()

    print(f"\nLast proof: {last_proof} -- Searching for next proof..\n")
    proof = random.randint(0, 999999)
    #  TODO: Your code here
    last = f"{last_proof}".encode()
    last_hash = hashlib.sha256(last).hexdigest()

    while valid_proof(last_hash, proof) is False:
        if timer() - start < 1:
            proof += 2
        else:
            return proof
    print(f"Proof found: {proof} in {timer() - start:.3f}s")
    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?

    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """
    # TODO: Your code here!
    guess = f"{proof}".encode()
    guess_hash = hashlib.sha256(guess).hexdigest()

    return last_hash[-6:] == guess_hash[:6]


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()

    r = requests.get(url=node + "/totals")
    data = r.json()
    if data['totals'][id]:
        coins_mined = data['totals'][id]
    else:
        coins_mined = 0

    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()

        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print(f"\nTotal coins mined: {coins_mined}\n")
        else:
            print(data.get('message'))
