#
# @lc app=leetcode id=443 lang=python
#
# [443] String Compression
#

# @lc code=start
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0  # Pointer to write the compressed characters
        read = 0   # Pointer to read through the `chars` array

        while read < len(chars): #process every character 
            char = chars[read]
            count = 0

            # Count the occurrences of the current character
            while read < len(chars) and chars[read] == char: #a
                read += 1
                count += 1

            # Write the character to the 'chars' array
            chars[write] = char # char[0] = a
            write += 1

            # If count > 1, append the count to the list
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write

# @lc code=end

"""

For chars = ["a", "a", "b", "b", "c", "c", "c"]:
First Pass:
Character a is counted (2 times).
Write 'a' to chars[0], and 2 to chars[1].
Now chars = ["a", "2", "b", "b", "c", "c", "c"], write = 2.
Second Pass:

Character b is counted (2 times).
Write 'b' to chars[2], and 2 to chars[3].
Now chars = ["a", "2", "b", "2", "c", "c", "c"], write = 4.
Third Pass:

Character c is counted (3 times).
Write 'c' to chars[4], and 3 to chars[5].
Now chars = ["a", "2", "b", "2", "c", "3", "c"], write = 6.
Final Result:

The function returns write = 6, and the first 6 elements of chars are the compressed list: ["a", "2", "b", "2", "c", "3"].
"""
"""
        i = 0
        n = len(chars)
        while i < n:
            char = chars[i]
            count = 0
            chars.append(char)
            while i <= n:
                if(chars[i] == char and i != n):
                    count += 1
                    i += 1
                else:
                    if(count >= 10):
                        for digit in str(count):
                            chars.append(digit)
                    elif(count == 1):
                        break
                    else:
                        chars.append(str(count))
                    break
        chars[:] = chars[n:]
        return len(chars)


"""
