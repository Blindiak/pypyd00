import sys

arg = sys.argv
del arg[0]

usage = "Usage: python operations.py <number1> <number2>\n" \
        "Example:\n" \
        "         python operations.py 10 3"


if len(arg) != 2:
    print("InputError: too many arguments\n")
    print(usage)
    exit(0)

if not(arg[0].isnumeric()) or not(arg[1].isnumeric()):
    print("InputError: only numbers\n")
    print(usage)
    exit(0)

nb1 = int(arg[0])
nb2 = int(arg[1])

print("Sum:        " + str(nb1 + nb2))
print("Difference: " + str(nb1 - nb2))
print("Product:    " + str(nb1 * nb2))
if nb2 == 0:
    print("Quotient:   ERROR(div by zero)")
else:
    print("Quotien:    " + str(nb1 / nb2))
if nb2 == 0:
    print("Remainder:  ERROR (modulo by zero)")
else:
    print("Remainde:   " + str(nb1 % nb2))
