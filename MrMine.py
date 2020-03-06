import hashlib
import requests
import time
import sys
from uuid import uuid4
from timeit import default_timer
import random
import json

def proofer(last_proof):
    start = default_timer()

    print("Searching for proof")
    proof = random.randint()