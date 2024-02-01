def calculate_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


result1 = calculate_sum(1, 2, 3, 4, 5)
print(result1)  # Output: 15

result2 = calculate_sum(10, 20, 30)
print(result2)  # Output: 60

result3 = calculate_sum(2, 4, 6, 8, 10, 12, 14)
print(result3)  # Output: 56


def calculate_sum(message, *numbers):
    total = 0
    for num in numbers:
        total += num
    print(message, total)


calculate_sum("The sum is:", 1, 2, 3, 4, 5)
# Output: The sum is: 15


if __name__ == "__main__":
    pass
