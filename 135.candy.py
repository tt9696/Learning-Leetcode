#
# @lc app=leetcode id=135 lang=python
#
# [135] Candy
# need to distribute candies to children such that each child receives at least one candy, children with a higher rating than their neighbors receive more candies than them, and we minimize the total number of candies used.

# @lc code=start
# ratings = [1,0,2]
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        left_to_right = [1]* n
        right_to_left = [1]* n
        total_candies = 0

        for i in range(1, n):
            #compare the left element i=1
            if ratings[i] > ratings[i-1]:#if ratings is higher than previous
                left_to_right[i] = left_to_right[i-1] + 1  #[1, 1, 2]
        
        for i in range(n-2,-1,-1):
            #compare the right element, start at second-to-last index, stop:-1 to include index 0 , step at decrements the index by 1
            # [1,0,2] start at 0
            if ratings[i] > ratings[i+1]:
                right_to_left[i] = right_to_left[i+1] + 1 # [2, 1, 1]

        for j in range(n):
            total_candies += max(left_to_right[j], right_to_left[j])
            # max(1,2) + max(1,1) + max(2,1) = 2+1+2 = 5
        return total_candies

# @lc code=end

