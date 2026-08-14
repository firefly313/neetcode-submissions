class Solution:
    def isValid(self, s: str) -> bool:
        valid = ['(', ')', '{', '}', '[', ']']
        ## stack, lifo
        ## uses append and pop
        stack = []
        ## 3 diff typeds of bracket
        for let in s:
            ## append stack
            if let == '(':
                stack.append('(')
            if let == '{':
                stack.append('{')
            if let == '[':
                stack.append('[')
            ## pop stack
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
        
        ## i: 0 to i: 5
        ## example s = "[(])"
        ## i = 0, let = [, stack = ['[']
        ## i = 1, let = (, stack = ['[', '(]
        ## i = 2, let = ], is stack[-1] ] stack =
        ## i = 3,

        ## stack, append 1 for parenthesis
        ## pop if other parenthesis
        ## if stack ends up being empty, return true
        ## if it isnt empty, return false