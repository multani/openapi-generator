# flake8: noqa

import random


def id_gen(bits: int=32) -> int:
    """ Returns a n-bit randomly generated int """
    return int(random.getrandbits(bits))
