class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            ss = ''.join(sorted(s))
            group[ss].append(s)
        return [value for value in group.values()]
            