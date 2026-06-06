class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftSum = [0]
        app = 0
        for i in nums:
            app += i
            leftSum.append(app)
        rightSum = [0]
        app = 0
        for i in nums[::-1]:
            app += i
            rightSum.append(app)
        rightSum, leftSum = rightSum[:-1][::-1], leftSum[:-1]
        answer = []
        for index in range(len(nums)):
            answer.append(abs(leftSum[index] - rightSum[index]))
        return answer


    
#test
a = Solution()
nums = [10,4,8,3]
print(a.leftRightDifference(nums))