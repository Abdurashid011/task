class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        x = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for close in s:
            if close in x:
                lst.append(close)
            elif len(lst) == 0 or close != x[lst.pop()]:
                return False

        return len(lst) == 0

print(Solution().isValid("()[]{}"))

