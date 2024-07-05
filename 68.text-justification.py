#
# @lc app=leetcode id=68 lang=python
#
# [68] Text Justification
#

# @lc code=start
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
       
        current_line = []
        num_of_letter = 0
        for word in words:
            if num_of_letter + len(word) + len(current_line) >  maxWidth:#num_of_letters + len("example") + len(current_line) = 8 + 7 + 3 = 18
                for i in range(maxWidth - num_of_letter): # calculates the total number of spaces that need to be distributed: maxWidth - num_of_letters = 16 - 8 = 8
                    current_line[i % (len(current_line)-1 or 1)] += ' '
                
                result.append(''.join(current_line))
                current_line, num_of_letter = [], 0

            current_line += [word]
            num_of_letter += len(word)

        #Join the words and left-justify
        result.append(' '.join(current_line).ljust(maxWidth)) #banana              is my favorite fruit.
        return result

    """
    maxWidth = 16
    current_line = ["This", "is", "an"]
    Adding "example":
    Current line length with spaces: num_of_letters + len("example") + len(current_line) = 8 + 7 + 3 = 18
    18 exceeds maxWidth, so we need to justify the current line.
    maxWidth - num_of_letters = 16 - 8 = 8
    len(current_line) = 3 
    i = 0,1,2,3,4,5,6,7
    0 % (3 - 1) = 0 % 2 = 0
    current_line[0] += " " ==> current_line = ["This ", "is", "an"]
    1 % (3 - 1) = 1 % 2 = 1
    current_line[1] += " " ==> current_line = ["This ", "is ", "an"]
    current_line[0] += " " ==> current_line = ["This  ", "is ", "an"]
    current_line[1] += " "
    current_line[0] += " "
    current_line[1] += " "
    current_line[0] += " "
    current_line[1] += " "

    result = ["This    is    an", "example  of text"]
    """

        
# @lc code=end

