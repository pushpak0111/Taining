def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num
if __name__ == '__main__':
    num = int(input("Enter a number: "))
    result = reverse_number(num)
    print("Reversed number:", result)
