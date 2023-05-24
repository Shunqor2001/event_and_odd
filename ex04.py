var_int = 1234
var_str = str(var_int)
sum_even = 0

for digit in var_str:

    if int(digit) % 2 == 0:
        sum_even += int(digit)

print("Sum of even digits:", sum_even)