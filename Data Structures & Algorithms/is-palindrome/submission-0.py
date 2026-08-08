class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        print(s)
        left = 0 
        right = len(s) - 1

        for i in range(len(s)):
            
           
            if s[left] == s[right]:
                left+=1
                right-=1
                
                continue
            else:
                return False

        return True