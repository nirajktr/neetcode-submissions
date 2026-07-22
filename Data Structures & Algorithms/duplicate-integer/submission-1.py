class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list2 = []
        for i in nums:
            if i not in list2:
                list2.append(i)
        
        return len(nums) > len(list2)
            