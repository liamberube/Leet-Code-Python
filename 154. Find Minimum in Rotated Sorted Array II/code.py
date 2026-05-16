class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = -5000
        for ele in nums:
            if ele < prev:
                return ele
            prev = ele
        return nums[0]

#test case
a = Solution()
nums = [2,2,2,0,1]
print(a.findMin(nums))