# -*- coding: utf-8 -*-
# Time    : 2019/12/5 21:07
# Author  : Tianxiao Gao
# Contact : gtx@pku.edu.cn
# File    : 4.py
"""
Description : Median of Two Sorted Arrays
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0:
            if len(nums2) % 2 == 1:
                return nums2[len(nums2) // 2]
            else:
                return (nums2[len(nums2) // 2 - 1] + nums2[len(nums2) // 2]) / 2
        if len(nums2) == 0:
            if len(nums1) % 2 == 1:
                return nums1[len(nums1) // 2]
            else:
                return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
        length = len(nums1) + len(nums2)
        p1 = 0
        p2 = 0
        medium = 0
        while True:
            if p1 == len(nums1):
                p2 += 1
            elif p2 == len(nums2):
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
            if length % 2 == 1 and p1 + p2 == length // 2:
                if p1 == len(nums1):
                    return nums2[p2]
                elif p2 == len(nums2):
                    return nums1[p1]
                elif nums1[p1] < nums2[p2]:
                    return nums1[p1]
                else:
                    return nums2[p2]
            elif length % 2 == 0 and p1 + p2 == length // 2 - 1:
                if p1 == len(nums1):
                    medium += nums2[p2]
                elif p2 == len(nums2):
                    medium += nums1[p1]
                elif nums1[p1] < nums2[p2]:
                    medium += nums1[p1]
                else:
                    medium += nums2[p2]
            elif length % 2 == 0 and p1 + p2 == length // 2:
                if p1 == len(nums1):
                    return (medium + nums2[p2]) / 2
                elif p2 == len(nums2):
                    return (medium + nums1[p1]) / 2
                elif nums1[p1] < nums2[p2]:
                    return (medium + nums1[p1]) / 2
                else:
                    return (medium + nums2[p2]) / 2


num1 = [1, 2]
num2 = [3, 4]
sol = Solution()
print(sol.findMedianSortedArrays(num1, num2))
