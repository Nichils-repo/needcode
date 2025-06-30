class Solution:
    def isValid(self, s: str) -> bool:
        
        stack =[]
        hashmap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for chara in s: 
            if chara in hashmap:
                if stack and stack[-1] == hashmap(chara):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(chara)
            
        return True if not stack else False
