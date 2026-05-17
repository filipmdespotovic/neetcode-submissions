class Solution:
    def isValid(self, s: str) -> bool:
        stek = []
        for c in s:
            if c == "[" or c == "(" or c == "{":
                stek.append(c)
            else:
                if len(stek) == 0:
                    return False
                if c == "]":
                    if stek[-1] != "[":
                        return False

                if c == "}":
                    if stek[-1] != "{":
                        return False

                if c == ")":
                    if stek[-1] != "(":
                        return False

                stek.pop()

        if len(stek) == 0:
            return True
        return False