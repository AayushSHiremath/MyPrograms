def countdigits(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

n=int(input("Enter the number: "))
print(f"The Number is {n}")
d = countdigits(n)
print(f"Number of digits {d}")