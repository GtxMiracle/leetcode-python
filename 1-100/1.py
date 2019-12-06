# -*- coding: utf-8 -*-
# Time    : 2019/11/26 22:13
# Author  : Tianxiao Gao
# Contact : gtx@pku.edu.cn
# File    : 1.py
"""
Description :  Two Sum
"""


class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [hashmap.get(target - num), i]
            hashmap[num] = i


sol = Solution()
print(sol.twoSum([1, 2, 3, 4, 8], 10))
