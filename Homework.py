number = int(input("Enter a whole number: "))

digit_count = 0

if number == 0:
    digit_count = 1

if number < 0:
    number = -number

while number > 0:
    digit_count += 1
    number = number // 10

print("The number of digits is:", digit_count)
