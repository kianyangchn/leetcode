# -*- coding: utf-8 -*-
# @Author: kianyangchn
# @Date:   2018-03-04 09:09:47
# @Last Modified by:   kianyangchn
# @Last Modified time: 2018-03-04 09:21:48


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        st = 0
        ed = len(nums) - 1
        while st <= ed:
            mid = (st + ed) // 2
            if nums[st] < nums[ed]:
                return nums[st]
            else:
                if nums[mid] < nums[ed]:
                    ed = mid - 1
                elif: nums[mid] > nums[st]
                    st = mid + 1
                elif: nums[mid] == nums[st]:
                    return nums[ed]
