# -*- coding: utf-8 -*-
# Time    : 2019/12/5 19:40
# Author  : Tianxiao Gao
# Contact : gtx@pku.edu.cn
# File    : 3.py
"""
Description : Longest Substring Without Repeating Characters
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        current_string = ""
        char_list = []

        for i in range(len(s)):
            end = True
            sub_s = s[i:]
            for char in sub_s:
                if char in char_list:
                    length = len(current_string)
                    if length > max_length:
                        max_length = length
                    current_string = ""
                    char_list = []
                    end = False
                    break
                else:
                    current_string += char
                    char_list.append(char)
            if end is True:
                length = len(sub_s)
                if length > max_length:
                    max_length = length
                current_string = ""
                char_list = []
                end = False
        return max_length


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans


sol = Solution()
ss = "aebcfba"
print(sol.lengthOfLongestSubstring(ss))
