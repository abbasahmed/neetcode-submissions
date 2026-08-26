class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]

        hashmap = {}
        
        for word in strs:
            cmap = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                cmap[idx] += 1
            key = tuple(cmap)
            if key in hashmap:
                hashmap[key].append(word)
            else: 
                hashmap[key] = [word]
        
        return list(hashmap.values())
