from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = defaultdict(int)
        anagram = []
        for string in strs:
            sorted_string = sorted(string)
            sorted_string = "".join(sorted_string)
            if not sorted_dict[sorted_string]:
                sorted_dict[sorted_string] = len(sorted_dict)
            sid = sorted_dict[sorted_string] - 1
            if len(anagram) == sid:
                anagram.append([string])
            else:
                anagram[sid].append(string)
                
        return anagram


## 책 풀이
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())