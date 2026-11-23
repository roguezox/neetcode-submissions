class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        seens = {}
        seent = {}
        
        for character in s:
           seens[character] = seens.get(character,0) + 1 
        for character in t:
            seent[character] = seent.get(character, 0) + 1
        return seens == seent