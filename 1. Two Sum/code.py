class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            somme = nums[i]
            for j in range(i + 1, len(nums)):
                if somme + nums[j] == target:
                    return [i, j]