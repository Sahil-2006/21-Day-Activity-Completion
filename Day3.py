# Functions + Modular Programming
# 1. Writing clean functions
# 2. Handling edge cases
# 3. Modular code structure

# Function 1: Safe Division
def safe_divide(a, b):
    """
    Divide a by b safely.
    Edge cases handled:
        - b = 0 (division by zero)
        - non-number inputs
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Inputs must be numbers"

    if b == 0:
        return "Error: Division by zero"

    return a / b

# Function 2: Find Maximum in List
def find_max(lst):
    """
    Return the maximum number in a list.
    Edge cases handled:
        - empty list
        - list with non-numeric values
    """
    if not lst:
        return "Error: List is empty"

    for x in lst:
        if not isinstance(x, (int, float)):
            return "Error: List contains non-numeric value"

    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

# Function 3: Check Palindrome
def is_palindrome(text):
    """
    Check if a string is a palindrome.
    Edge cases handled:
        - empty string
        - spaces/case sensitivity
    """
    if not isinstance(text, str):
        return "Error: Input must be a string"

    cleaned = text.replace(" ", "").lower()

    if cleaned == "":
        return "Error: String is empty"

    return cleaned == cleaned[::-1]

# Function 4: Fibonacci Generator
def generate_fibonacci(n):
    """
    Return first n Fibonacci numbers.
    Edge cases handled:
        - negative numbers
        - non-integer input
        - n = 0
    """
    if not isinstance(n, int):
        return "Error: n must be an integer"

    if n < 0:
        return "Error: n cannot be negative"

    if n == 0:
        return []

    if n == 1:
        return [0]

    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


# MAIN MODULE EXECUTION
if __name__ == "__main__":
    print("Safe Divide:", safe_divide(10, 2))
    print("Safe Divide (Zero):", safe_divide(10, 0))
    print("Find Max:", find_max([1, 5, 3, 9, 2]))
    print("Find Max (Error):", find_max([]))
    print("Palindrome:", is_palindrome("Racecar"))
    print("Palindrome:", is_palindrome(""))
    print("Fibonacci:", generate_fibonacci(10))
    print("Fibonacci (Negative):", generate_fibonacci(-5))

# 5 Additional Questions
# 1. Running Sum of 1D Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
    
# 2. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return [c + extraCandies >= m for c in candies]
# 3. Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer) for customer in accounts)
# 4. Number of Good Pairs
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
            freq = {}
            count = 0
            for n in nums:
                if n in freq:
                    count += freq[n]
                    freq[n] += 1
                else:
                    freq[n] = 1
            return count
# 5.Jewels and Stones
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0
        for ch in stones:
            if ch in s:
                count += 1
        return count
