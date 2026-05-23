class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        went_down = False
        prev = nums[-1]
        for num in nums:
            if num < prev:
                if went_down:
                    return False
                else:
                    went_down = True
            prev = num
        return True
    
#test
nums = [2,1,3,4]
a = Solution()
print(a.check(nums))