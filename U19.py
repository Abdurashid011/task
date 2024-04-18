class Solution:
    def calPoints(self, operations: list[str]) -> int:
        lst = []
        for i in operations:
            if i != 'C' and i != 'D' and i != '+':
                lst.append(int(i))
            elif i == 'C':
                lst.pop()
            elif i == 'D':
                x = lst[-1]
                x = x * 2
                lst.append(x)
            elif i == "+":
                y = lst[-1] + lst[-2]
                lst.append(y)
        return sum(lst)
                
print(Solution().calPoints(["5","2","C","D","+"]))