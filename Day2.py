# Python Conditions and Loops
age = 5
if(age>5):
    print("Age is greater than 5")
elif(age<5):
    if(age>0 and age!=4):
        print("Age is less than 5")
else:
    print("Your age is not 5")

msg = "Adult" if age >= 18 else "Child"
print(msg)

for i in range(5):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(10, 0, -1):
    print(i)

for x in [10, 20, 30]:
    print(x)

for ch in "python":
    print(ch)
i = 1

while i <= 5:
    print(i)
    i += 1
for i in range(10):
    if i == 5:
        break

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

if x == 5:
    pass  # do nothing yet

for i in range(5):
    print(i)
else:
    print("loop finished")

for i in range(3):
    for j in range(2):
        print(i, j)

# 5 Beginner Coding Problems 
# 1. Contains Duplicate Values
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in range(0,len(nums)):
            s.add(nums[i])
        if(len(s)==len(nums)):
            return False
        else:
            return True
# 2. Missing Number
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if nums[0] != 0:
            return 0
        for i in range(1, n):
            if nums[i] != nums[i-1] + 1:
                return nums[i-1] + 1
        
        return n
# 3. Two Sum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
# 4. How Many Numbers Are Smaller Than the Current Number
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        res = []
        n = len(nums)
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[j] < nums[i]:
                    count += 1
            res.append(count)
        return res
# 5. Minimum Time visiting all points
class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        time = 0
        
        for i in range(1, len(points)):
            x1, y1 = points[i-1]
            x2, y2 = points[i]
            
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            
            # You can move diagonally, so max(dx, dy) is enough
            time += max(dx, dy)
        
        return time
