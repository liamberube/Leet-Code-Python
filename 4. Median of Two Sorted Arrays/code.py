class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        lenght = len(nums)
        if lenght % 2 == 1:
            return nums[lenght//2]
        else:
            print((nums[lenght//2 - 1] + nums[lenght//2]))
            return ((nums[lenght//2 - 1] + nums[lenght//2]))/2


#test
a = Solution()
nums1 = [1,3]
nums2 = [2,4]
print(a.findMedianSortedArrays(nums1, nums2))