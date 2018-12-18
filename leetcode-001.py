# Brute force slow solution
class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(0, len(nums)):
            for y in range(x+1, len(nums)):
                if (nums[x]+nums[y] == target):
                    return [x,y]
        raise ValueError('No answer')

# Solution 2
# Loops through twice
class Solution2:
    def twoSum(self, nums, target):
        valuesSeen = {}
        for x in range(0, len(nums)):
            valuesSeen[nums[x]] = x
        for x in range(0, len(nums)):
            compliment = target - nums[x]
            if compliment in valuesSeen:
                return [x, valuesSeen[compliment]]

# Solution 3
# Loops through once
# Submitted Solution
class Solution3:
    def twoSum(self, nums, target):
        valuesSeen = {}
        for x in range (0, len(nums)):
            compliment = target - nums[x]
            if compliment in valuesSeen:
                return [valuesSeen[compliment], x]
            valuesSeen[nums[x]] = x

sol = Solution3()
answer = sol.twoSum([2,7,12,23], 9)
print(answer)