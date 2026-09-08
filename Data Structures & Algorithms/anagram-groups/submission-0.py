class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                code = ord(c) - ord('a')
                count[code] += 1
            hmap[tuple(count)].append(s)
        return hmap.values()