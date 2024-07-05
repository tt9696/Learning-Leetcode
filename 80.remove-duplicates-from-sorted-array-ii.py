#
# @lc app=leetcode id=80 lang=python
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        i = 1  # Pointer for the position of the last allowed element
        count = 1  # Count the occurrence of each element

        for j in range(1, len(nums)): #range(1,9) 
            #print(j) # 1,2,3,4,5,6,7,8
            #print(nums[j]) # 0,1,1,1,1,2,3,3
        
            if nums[j] == nums[j - 1]: # j=1 nums[1] == nums[0] , second is equal to first
                count += 1 # same number +1
            else:#j = 2: nums[2] != nums[1]  ==> 0,1
                count = 1 # reset count new element
            
            if count <= 2: # means the current element appears at most twice, so it can be added to the new position i.
                nums[i] = nums[j]  # nums[2] = nums[2]
                i += 1 # i =3 Increment i to move to the next position.
            return i

        # Sample Answer
        #---------------------------------------------
        # j = 1                                     # second element in the array; j=2=> third element
        # for i in range(1,len(nums)):              # range(1,9)
        #     if( j == 1 or nums[i] != nums[j-2] ): # j==1 meaning beginning; nums[i] != nums[-1] negative indices count from the end of the list. 
        #                                           # This condition ensures that the second element is always included in the new array, regardless of its value, because there is no previous element to compare with.
        #         nums[j] = nums[i]                 
        #         j +=1
        # return j
        

        #Now, j = 2 and i = 2:
        # Check the condition nums[i] != nums[j-2]:
        # nums[2] != nums[0]
        # 1 != 0 (true)
        # So, set nums[2] = nums[2] (no change).
        # Increment j to 3.
# @lc code=end

