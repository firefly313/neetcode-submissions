class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for let in s:
            if let == '(':
                stack.append('(')
            if let == '{':
                stack.append('{')
            if let == '[':
                stack.append('[')
            if let == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            if let == '}':
                if len(stack) != 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            if let == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else: 
            return False 


