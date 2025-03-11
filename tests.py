for number in range(1, 10):  # Loop through numbers 1 to 9
    if number == 5:
        print("Breaking the loop at 5")
        break  # Exit the loop when number is 5
    elif number % 2 == 0:
        print(f"Skipping {number} because it's even")
        continue  # Skip the rest of the loop body for even numbers
    print(f"Processing number: {number}")

x = int(input("Enter a number: "))
for i in range(1, 10):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")



for i in range(1, 10):
    for j in range(1, 10):
        if i % j == 0:
            print(f" outer loop: {i}  inner loop {j}")


for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"Outer loop: {i}, Inner loop: {j}")


def large_power(base, exponent):
    """Returns True if base raised to exponent is greater than 5000, otherwise False."""
    return base ** exponent > 5000

# Example usage
print(large_power(10, 3))  # True (10^3 = 1000, which is not greater than 5000)
print(large_power(5, 5))   # True (5^5 = 3125, which is not greater than 5000)
print(large_power(8, 4))   # True (8^4 = 4096, which is not greater than 5000)
print(large_power(10, 4))
print(large_power(base=10, exponent=5))
# True (10^4 = 10000, which is greater than 5000)

num=int(input("Enter a number: "))
def divisible_by_10(num):
    if num % 10 == 0:
        return True
    else:
        return False
print(divisible_by_10(num))


def divisible_by_10(num):
    """Returns True if num is divisible by 10, otherwise False."""
    return num % 10 == 0  # Directly returns the condition result

num = int(input("Enter a number: "))  # User input
print(divisible_by_10(num))


def divisible_by_10(num):
    return num % 10 == 0
num = int(input("Enter a number: "))
print(divisible_by_10(num))