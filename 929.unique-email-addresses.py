#
# @lc app=leetcode id=929 lang=python
#
# [929] Unique Email Addresses
#
# Rules for the local name:
#   - Ignore everything after a plus + sign.
#   - Remove all . dots.
# need combine back domain
# @lc code=start
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seen = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0] # get before +
            local = local.replace(".", "")# # remove all '.'
            new_email = local + "@" + domain
            seen.add(new_email)
        return len(seen) #return the number of different addresses that actually receive mails.
        
# @lc code=end

