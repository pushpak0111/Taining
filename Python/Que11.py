#mirror image of right angle triangle
def main():
    n = int(input())
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)
if __name__ == '__main__':
    main()