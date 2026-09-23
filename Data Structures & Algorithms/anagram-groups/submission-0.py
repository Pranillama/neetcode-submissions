
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # result = defaultdict will make the key itself with the value(list) 
        for s in strs:  # for every string in the strings
            count = [0] * 26 
            for c in s:  # for every character in the string(s)
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())  # <-- Correctly indented here
