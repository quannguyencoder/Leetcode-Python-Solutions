class Solution:
    def reverseParentheses(self, s: str) -> str:
        open_par = deque()
        result = []
        for current_char in s:
            if current_char == "(":
                open_par.append(len(result))
            elif current_char == ")":
                start = open_par.pop()
                result[start:] = result[start:][::-1]
            else:
                result.append(current_char)
        return "".join(result)