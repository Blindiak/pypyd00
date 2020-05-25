import string


def text_analyzer(*arg):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if len(arg) == 0:
        print("What is the text to analyse?")
        s = input()
    elif len(arg) > 1:
        print("ERROR")
        return
    else:
        s = arg[0]

    nb_l_l = 0
    nb_u_l = 0
    nb_space = 0
    nb_p_m = 0

    print("The text contains " + str(len(s)) + " characters:\n")

    for c in s:
        if c.islower():
            nb_l_l += 1
        elif c.isupper():
            nb_u_l += 1
        elif c == ' ':
            nb_space += 1
        elif c in string.punctuation:
            nb_p_m += 1

    print(str(nb_u_l) + " upper letters\n")

    print(str(nb_l_l) + " lower letters\n")

    print(str(nb_p_m) + " punctuation marks\n")

    print(str(nb_space) + " spaces")
