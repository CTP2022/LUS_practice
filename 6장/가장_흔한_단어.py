import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = paragraph.lower()
        p = re.sub("[^a-z0-9]"," ",p).split()
        p = Counter(p)
        p = p.most_common()
        for string,_ in p:
            if string not in banned:
                return string