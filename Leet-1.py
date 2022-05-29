# https://leetcode.com/problems/two-sum/
"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

import itertools
from typing import List

def sol1(nums, target):
    lst_cmb = list((idx_i,idx_j,i,j,i+j) for ((idx_i,i),(idx_j,j)) in itertools.combinations(enumerate(nums), 2))
    for elm_cmb in lst_cmb:
        if elm_cmb[4] == target:
            return (elm_cmb[0],elm_cmb[1])
    return list()

def sol2(nums, target):
    for idx_i, i in enumerate(nums):
        for idx_j, j in enumerate(nums):
            if idx_i != idx_j and i+j == target:
                return [idx_i, idx_j]
    return list()

def sol3(nums, target):
    lstSize = len(nums)
    for idx_i in range(0,lstSize-1):
        for idx_j in range(idx_i+1,lstSize):
            if nums[idx_i]+nums[idx_j] == target:
                return [idx_i, idx_j]
    return list()
def solOpt(nums, target):
    # https://leetcode.com/problems/two-sum/discuss/2045849/1LINER-O(n)timeBEATS-99.97-MEMORYSPEED-0ms-MAY-2022
    seen = {}
    for i, value in enumerate(nums): 
        remaining = target - nums[i] 
        if remaining in seen: 
            return [i, seen[remaining]]
        else:
            seen[value] = i
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return sol3(nums,target)
if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(f"nums:{nums}")
    print(f"target:{target}")
    print(f"output:{Solution().twoSum(nums,target)}")