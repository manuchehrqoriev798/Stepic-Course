n = int(input())
original_n = n
counter = 0
sum_digit = 0
mult_digit = 1

while n != 0:
    last_digit = n % 10
    counter = counter + 1
    sum_digit = sum_digit + last_digit
    mult_digit = mult_digit * last_digit
    n = n // 10
the_first_digit = original_n // 10**(counter-1)
last_digit = original_n % 10
sum_first_last_digit = the_first_digit + last_digit
middle_arifmetic_digit = sum_digit / counter
print(sum_digit, counter, mult_digit, middle_arifmetic_digit, the_first_digit,  sum_first_last_digit,  sep='\n')