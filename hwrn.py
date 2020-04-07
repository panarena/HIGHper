import uuid
import os

def hwRNG():
    i = 0
    while True:
        yield i, uuid.uuid4().int
        i = i + 1

for _ in hwRNG():
    print(_)
