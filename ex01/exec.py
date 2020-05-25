import sys


def reverse_slicing(s):
    return s[::-1]


arg = sys.argv
del arg[0]

r = " "
r = r.join(arg)

r = reverse_slicing(r)

rc = ''
for c in r:
    if c.islower():
        rc += c.upper()
    elif c.isupper():
        rc += c.lower()
    else:
        rc += c

print(rc)
