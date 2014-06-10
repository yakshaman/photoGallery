import random

def genString(size=32) :
    return '%030x' % random.randrange(16**size)
