number = int(input('Enter your number:'))
# number = 0
while True:
    number += 1
    if number >= 10:
        break
    if number % 10 == 0:
        continue
    print(number)
