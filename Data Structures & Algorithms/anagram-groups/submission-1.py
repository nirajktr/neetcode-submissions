class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = defaultdict(list)
        for i in strs:
            x[tuple(sorted(i))].append(i)
        return list(x.values())


        