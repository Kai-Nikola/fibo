# Palindrome
# Examples
# 101, 111,202,303,222 n

def palindrome(n):
    n = str(n)
    if str(n) == str(n)[::-1]:
        print("It is a palindrome")
    else:
        print("Is not Palindrome")


palindrome('deified')

