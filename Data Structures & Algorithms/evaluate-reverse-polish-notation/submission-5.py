class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stek = []
        val = 0
        for token in tokens:
            if token == "+":
                x1 = stek.pop()
                x2 = stek.pop()
                val = int(x2 + x1)
                stek.append(val)
            elif token == "-":
                x1 = stek.pop()
                x2 = stek.pop()
                val = int(x2 - x1)
                stek.append(val)
            elif token == "*":
                x1 = stek.pop()
                x2 = stek.pop()
                val = int(x2 * x1)
                stek.append(val)
            elif token == "/":
                x1 = stek.pop()
                x2 = stek.pop()
                val = int(x2 / x1)
                stek.append(val)
            else:
                stek.append(int(token))

        return stek[0]

