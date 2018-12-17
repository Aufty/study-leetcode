# Brute force slow solution

class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in nums:
            for y in range(x+1, len(nums)):
                if (nums[x]+nums[y] == target):
                    return [x,y]
        raise ValueError('No answer')

sol = Solution1()
answer = sol.twoSum([2,7,12,23], 9)
print(answer)


