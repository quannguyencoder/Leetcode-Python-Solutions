class Solution:
    def smallestSubsequence(self, s: str) -> str:
        visited = set()
        cnt = Counter(s)
        stack = []
        for char in s:
            cnt[char] -= 1
            if char in visited:
                continue
            while stack and stack[-1] > char and cnt[stack[-1]] > 0:
                visited.remove(stack.pop())
            stack.append(char)
            visited.add(char)
        return ''.join(stack)
