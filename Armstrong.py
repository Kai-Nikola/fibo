num = 153

str_num = str(num)
power = len(str_num)
operations = sum(int(x) ** power for x in str_num)
if num == operations:
    print("Armstrong number")
else:
    print("Not a armstrong number")

#
# for num in range(1, 10010):
#     num_str = str(num)
#     power = len(num_str)
#     total = sum(int(digit) ** power for digit in num_str)
#     if total == num:
#         print(num)
