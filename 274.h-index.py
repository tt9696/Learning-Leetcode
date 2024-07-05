#
# @lc app=leetcode id=274 lang=python
#
# [274] H-Index
#descending order and then find the largest number h such that the h-th element in the sorted list is greater than or equal to h.

# @lc code=start
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True) #[6, 5, 3, 1, 0]
        h=0
        for i, citation in enumerate(citations, start=1): #print(i, citation)
            if citation >= i:
                h = i
            else:
                break
        return h
    """
    number of citations (citation) is greater than or equal to the paper number (i). 
    If the number of citations is less than the paper number, it breaks out of the loop since further papers will have even fewer citations.
    
    print(i, citation)  
    1 6
    2 5
    3 3
    4 1
    5 0
    
    """
# @lc code=end

