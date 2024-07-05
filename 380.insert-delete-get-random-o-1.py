#
# @lc app=leetcode id=380 lang=python
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random
class RandomizedSet(object):

    def __init__(self):
        self.dict={}
        self.list=[]

    # Check if the value is already in the dictionary. If it is, return False.
    # If not, add the value to the list and record its index in the dictionary.
    # Return True
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    # Check if the value is in the dictionary. If it is not, return False.
    # If it is, get the index of the value from the dictionary.
    # Swap the value with the last element in the list and update the dictionary to reflect this change.
    # Remove the last element from the list and delete the value from the dictionary.
    # Return True.
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False
        index = self.dict[val]
        last_element = self.list[-1]
        #Swap val with the last element in the list
        self.list[index] = last_element
        self.dict[last_element] = index
        self.list.pop()
        del self.dict[val]

        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        value = random.choice(self.list)
        return value


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

