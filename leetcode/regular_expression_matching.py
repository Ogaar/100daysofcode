import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return p.fullmatch(p,s)
         