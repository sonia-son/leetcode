class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[-i - 1]: # len(s)-1 - 1 
                    return False
            return True
        
        def dfs(s, tmp): 
            if len(s) == 0: 
                result.append(tmp)
                return 
            
            for i in range(len(s)): 
                prefix = s[:i + 1] 
                postfix = s[i + 1:] 
                
                if(isPalindrome(prefix)):
                    dfs(postfix, tmp + [prefix]) 
        result = []
        dfs(s, []) 
        return result 