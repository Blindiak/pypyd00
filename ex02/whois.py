import sys

arg = sys.argv
del arg[0]

if len(arg) != 1:
    print("ERROR")
    exit()

for check in arg[0]:
    if not(check.isnumeric()):
        print("ERROR")
        exit()

nb = int(arg[0])

if nb % 2 == 0:
    print("I'm Even.")
elif nb == 0:
    print("I'm Zero.")
else:
    print("I'm Odd.")
