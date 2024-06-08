# Task 1:
# Difference between Sums of Odd and Even Digits in a given number(use functions)
def diff_bet_sum_odd_even(datas):
    odd_sum = 0
    even_sum = 0
    for item in datas:
        if item % 2 == 0:
            even_sum += 1
        else:
            odd_sum += 1

    return odd_sum - even_sum


data = [2, 3, 6, 5, 4, 1, 7, 9, 8]
result = diff_bet_sum_odd_even(data)
print('Result:', result)
