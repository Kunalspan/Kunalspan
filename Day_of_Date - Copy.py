x = int(input("ENTER DAY: "))
y = int(input("ENTER MONTH: "))
z = int(input("ENTER YEAR: "))
day = int()
month = int()
year = int()
leap_year = int()
extra = int()

if 1 <= x <= 31:
    day = x + day
else:
    print("Invalid day ")
# print(day)

if y == 2 or y == 3 or y == 11:
    month = 3

elif y == 4 or y == 7:
    month = 6
elif y == 9 or y == 12:
    month = 5
elif y == 10 or y == 1:
    month = 0
elif y == 5:
    month = 1
elif y == 8:
    month = 2
elif y == 6:
    month = 4
else:
    print("Invalid value should be between 1-12")
# print(month)

if 1900 <= z <= 1999:
    year = (z % 100)
elif 2000 <= z <= 2800:
    year = z - 1900
else:
    print("Not valid year: ")
# print(year)
if z % 4 == 0 or z % 100 == 0 or z % 400 == 0:
    extra = (-1)
else:
    extra = 0
# print(extra)

leap_year = (year // 4)
# print(leap_year)

total = ((day + month + year + leap_year + extra) % 7)
# print(total)


if total == 0:
    print("It's Sunday!")
elif total == 1:
    print("It's Monday!")
elif total == 2:
    print("It's Tuesday!")
elif total == 3:
    print("It's Wednesday!")
elif total == 4:
    print("It's Thursday!")
elif total == 5:
    print("It's Friday!")
elif total == 6:
    print("It's Saturday!")
else:
    print("Invalid Input")
