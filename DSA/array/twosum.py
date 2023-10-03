class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in hm:
                return [i, hm[difference]]
            hm[n] = i

#Time-complexity: O(n)
#Space-complexity: O(n)