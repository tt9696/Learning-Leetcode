#
# @lc app=leetcode id=30 lang=python
#
# [30] Substring with Concatenation of All Words
# https://www.youtube.com/watch?v=-wlDdMmaYwI&t=828s

# @lc code=start
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        """
        s = "barfoothefoobarman"
        words= ["foo","bar"]
        output = [0,9]
        012 345 678 9
        bar foo the foobarman
        ^           ^
        Iteration 1 (i = 0)
        Current window: "barfoo" (from index 0 to 5)
        For j = 0:
        current_word = 0 + 0 * 3 = 0
        First word: s[0:3] = "bar"
        "bar" is in word_freq, add to current_word: {"bar": 1}
        For j = 1:
        current_word = 0 + 1 * 3 = 3
        Second word: s[3:6] = "foo"
        "foo" is in word_freq, add to current_word: {"bar": 1, "foo": 1}
        All words match, append 0 to result.

        While Loop:
        Check current_word = s[j:j + eachword_length] = "barfoo".
        Add "barfoo" to substring_freq.
        Increment j by eachword_length to j = 3.
        Continue until j = 6.
        Condition j == i + window_length is true (6 == 0 + 6).
        Append i = 0 to result.

        Iteration 2 (i = 1):
        Start with i = 1.
        substring_freq = {}, j = 1.
        While Loop:
        Check current_word = s[j:j + eachword_length] = "arfooth".
        "arfooth" is not in word_freq, break out of loop.
        Condition j == i + window_length is false (6 != 1 + 6), so no append.
        """

        if not s or not words:
            return []
        
        word_freq = {}
        for word in words:
            word_freq[word] = 1 + word_freq.get(word, 0)
        # store word inside -> word_freq = {"foo": 1, "bar": 1}

        eachword_length = len(words[0])#3 #foo: 3 characters long
        word_length = len(words) # 2 
        window_length = word_length*eachword_length #6

        result = []

        for i in range(len(s) - window_length + 1): # 0 through 12  (18-6+1)
            substring_freq ={}
            j = i
            while j < i + window_length:
                current_word = s[j:j + eachword_length] # s[0:3]

                if current_word not in word_freq:
                    break
                substring_freq[current_word] = substring_freq.get(current_word,0) + 1 # add frequency into substring_freq 

                if substring_freq[current_word] > word_freq[current_word]:
                    break
                j += eachword_length #j =3 b->f->t

            if j == i + window_length: #j ends at 6 (i + window_length)
                result.append(i)

        return result

"""
Other solution:
        if not s or not words:
            return []
        
        word_length = len(words[0])
        total_length = word_length * len(words)
        word_count = {}
        
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        result = []
        
        for i in range(word_length):
            left = i
            right = i
            curr_count = {}
            while right + word_length <= len(s):
                word = s[right:right + word_length]
                right += word_length
                if word in word_count:
                    curr_count[word] = curr_count.get(word, 0) + 1
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        curr_count[left_word] -= 1
                        left += word_length
                    if right - left == total_length:
                        result.append(left)
                else:
                    curr_count.clear()
                    left = right
        return result



"""


# @lc code=end

