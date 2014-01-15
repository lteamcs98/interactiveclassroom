# count_digits.py
# CS 1 class example by Devin Balkcom.

digits = [0, 3, 2, 3, 4, 3, 2, 2, 1, 7, 6, 4, 5, 8, 3, 2, \
          1, 2, 1, 1, 1, 0, 0, 0, 2, 2, 3, 4, 5, 6, 2, 9, 8]

counter_list = [0] * 10
for digit in digits:
    counter_list[digit] += 1

print counter_list
