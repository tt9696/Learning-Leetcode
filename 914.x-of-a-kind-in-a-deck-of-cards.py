#
# @lc app=leetcode id=914 lang=python
#
# [914] X of a Kind in a Deck of Cards
#  return true if and only if you can group the cards into one or more groups of X cards, where:
# All the cards in each group have the same integer.
# X is at least 2.

# @lc code=start

from collections import Counter
#from math import gcd
from fractions import gcd #Python 2
#from functools import reduce

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        #deck = [1,2,3,4,4,3,2,1]
        count = Counter(deck) # count = {1:2, 2:2, 3:2, 4:2}
        
        values = list(count.values()) # values = [2, 2, 2, 2]
    
        # Compute GCD manually
        current_gcd = values[0] #current_gcd = 2
        for v in values[1:]:
            current_gcd = gcd(current_gcd, v) #gcd(2, 2) → 2
        
        return current_gcd >= 2 #current_gcd = 2
        
# @lc code=end
"""
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    values = count.values() #dict_values([2, 2, 2, 2])
    #reduce(f, [a, b, c, d]) 
    #= f(f(f(a, b), c), d)
    group_size = reduce(gcd, values) # gcd(2,2,2,2) = 2 → ✅ return True

    # Step 1: gcd(2, 2) = 2
    # Step 2: gcd(2, 2) = 2
    # Step 3: gcd(2, 2) = 2

    # Final group_size = 2
    return group_size >= 2

"""
"""
def hasGroupsSizeX(deck):
    # Step 1: Count the frequency of each number manually
    freq = {}
    for num in deck:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 2: Compute the GCD of all frequencies
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # Initialize the GCD using the first frequency
    vals = list(freq.values())
    group_size = vals[0]
    for i in range(1, len(vals)):
        group_size = gcd(group_size, vals[i])

    # Step 3: Check if the GCD is at least 2
    return group_size >= 2




"""
