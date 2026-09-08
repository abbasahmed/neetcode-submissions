class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counters_s = defaultdict(int)
        counters_t = defaultdict(int)
        for i in s:
            counters_s[i] += 1
        for i in t:
            counters_t[i] += 1
        
        for k in counters_s.keys():
            if k not in counters_t:
                return False
            else:
                if counters_s[k] != counters_t[k]:
                    return False
        return True