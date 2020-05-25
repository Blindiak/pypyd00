import sys
import string

if len(sys.argv) != 3:
    print("ERROR")
    exit(1)

try:
    mini = [w for w in "".join([c for c in sys.argv[1] if c not in
                                string.punctuation]).split(" ") if
            len(w) > int(sys.argv[2])]
    if len(mini) == 0:
        print("ERROR")
        exit(1)
    else:
        print(mini)
except ValueError:
    print("ERROR")
    exit(1)
