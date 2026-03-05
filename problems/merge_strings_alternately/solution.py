class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        n1, n2 =len(word1), len(word2)
        for i in range(min(n1, n2)):
            merged.append(word1[i])
            merged.append(word2[i])
        
        limit=min(n1,n2)
        merged.append(word1[limit:])
        merged.append(word2[limit:])    
        return ''.join(merged)
