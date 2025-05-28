#
# @lc app=leetcode id=1491 lang=python
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        total = sum(salary)
        max_salary = max(salary)
        min_salary = min(salary)
        adjusted_sum = total - max_salary - min_salary
        count = len(salary) - 2
        return adjusted_sum / count
# @lc code=end
"""
wrong answer for test case 
[48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]

def average(salary):
    total = sum(salary)
    max_salary = max(salary)
    min_salary = min(salary)
    adjusted_sum = total - max_salary - min_salary
    count = len(salary) - 2
    return adjusted_sum / count

    Cannot if got two min or two max
def average(salary):    
    minSalary = min(salary)
    maxSalary = max(salary)

    total = 0

    for s in salary:
        if s != minSalary and s != maxSalary:
            total += s
    return total / len(salary) - 2

"""
