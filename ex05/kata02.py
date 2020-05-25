date = (3, 30, 2019, 9, 25)

day = str(date[3])
month = str(date[4])
year = str(date[2])
hour = str(date[0])
minute = str(date[4])

if len(day) == 1:
    day = "0" + day

if len(month) == 1:
    month = "0" + month

if len(minute) == 1:
    minute = "0" + minute

if len(hour) == 1:
    hour = "0" + hour

print(day + "/" + month + "/" + year + " " + hour + ":" + minute)
