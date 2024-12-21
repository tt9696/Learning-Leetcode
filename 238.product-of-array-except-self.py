#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
# return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
# [1,2,3,4] 2*3*4= 24 1*3*4=12 1*2*4==> [24,12,8]
# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer= [1] * len(nums) #[1, 1, 1, 1]

        left_product = 1
        for i in range(n):#0 1 2 3
            answer[i] = left_product #[1,1,1,1]
            left_product*=nums[i]

        right_product =1
        for i in reversed(range(n)): #3 2 1 0
            answer[i] *= right_product
            right_product  *= nums[i]
        
        return answer
    
    """
    [1,2,3,4]
    i = 0 (1) => left: 1, right:2*3*4=24
    i = 1 (2) => left: 1, right:3*4=12
    i = 2 (3) => left: 1*2=2, right:4
    i = 3 (4) => left: 1*2*3=6, right=1
    [1,1,2,6] [24,12,4,1] ==> [24,12,8,6]

    nums =[1,2,3,4]
    Left Products:
    For i = 0: left_product = 1, answer = [1, 1, 1, 1]
    For i = 1: left_product = 1 * 1 = 1, answer = [1, 1, 1, 1]
    For i = 2: left_product = 1 * 2 = 2, answer = [1, 1, 2, 1]
    For i = 3: left_product = 2 * 3 = 6, answer = [1, 1, 2, 6]
    answer = [1, 1, 2, 6]

    Right Products and Combine:
    answer[i] *= right_product, right_product*=nums[i]
    For i = 3: answer[3] * 1 = 6, right_product= 1* 4 = 4
    For i = 2: answer[2] * 4 = 8, right_product = 4 * 3 = 12
    For i = 1: answer[1] * 12 = 12, right_product = 12 * 2  = 24
    For i = 0: answer[0] * 24 = 24, right_product = 24 * 1 = 24
    answer = [24, 12, 8, 6]
    
    ------time limit exceeded-----
        for i in range(len(nums)):
        product = 1
        for j in range(n):
            if i != j:
                product = product * nums[j]
        answer[i] = product
    return answer
    """
# @lc code=end

