t = (0, 4, 132.42222, 10000, 12345.67)

nb_day = str(t[0])
if len(str(nb_day)) == 1:
    nb_day = "0" + str(nb_day)
day = "day_" + str(nb_day)

nb_ex = str(t[1])
if len(str(nb_ex)) == 1:
    nb_ex = "0" + nb_ex
ex = "day_" + nb_ex

f = ("%f" % t[2])

s1 = ("%.2e" % t[3])

s2 = ("%.2e" % t[4])

print(day + " " + ex + " " + f + " " + s1 + " " + s2)
