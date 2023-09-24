"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

numbers.sort()

n = len(numbers)
ans = 0

if n % 2 == 0:
    n = int(n / 2)
    ans = (numbers[n] + numbers[n + 1]) / 2

if n % 2 == 1:
    n = int(n / 2)
    ans = numbers[n]
print(ans)
