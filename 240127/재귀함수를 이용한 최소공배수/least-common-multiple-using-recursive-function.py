import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm_recursive(numbers, n):
    if n == 1:
        return numbers[0]
    else:
        return (numbers[n-1] * lcm_recursive(numbers, n-1)) // gcd(numbers[n-1], lcm_recursive(numbers, n-1))

def find_lcm(numbers):
    if not numbers:
        return None
    return lcm_recursive(numbers, len(numbers))

# 예시
input_numbers = [4, 6, 8, 10]
result = find_lcm(input_numbers)
print(f"주어진 수들의 최소공배수: {result}")