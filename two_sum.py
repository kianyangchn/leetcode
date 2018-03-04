# -*- coding: utf-8 -*-
# @Author: kianyangchn
# @Date:   2018-03-04 08:50:57
# @Last Modified by:   kianyangchn
# @Last Modified time: 2018-03-04 08:59:48


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index_map = dict()
        for i in range(0, len(nums)):
            num = nums[i]
            if num in num_index_map:
                return [num_index_map[num], i]
            else:
                num_index_map[target - num] = i
