from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        result = []

        for s in strs:
            s_sort=tuple(sorted(s))
            anagramMap[s_sort].append(s)
        
        for value in anagramMap.values():
            result.append(value)
        
        return result