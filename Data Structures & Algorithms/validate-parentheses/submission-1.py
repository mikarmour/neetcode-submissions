class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2: 
            return False
        stack = []
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if stack[-1] != matching[bracket]:
                    return False
                stack.pop()

        return len(stack) == 0