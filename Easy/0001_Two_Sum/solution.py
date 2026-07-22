class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            current = nums[i]
            need = target - current

            if need in hashmap:
                return [hashmap[need], i]

            hashmap[current] = i