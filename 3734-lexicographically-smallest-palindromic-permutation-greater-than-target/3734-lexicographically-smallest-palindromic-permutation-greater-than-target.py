class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freg = Counter(s)
        odd_chars = [c for c in freg if freg[c] % 2 == 1]
        if len(odd_chars) > 1:
            return ''
        mid_char = odd_chars[0] if odd_chars else ''
        for c in freg:
            freg[c] //= 2
        half_n = n // 2
        choosen = []
        sorted_char = [c for c in sorted(freg) if freg[c] > 0]

        def dp(idx, tight):
            j = n - 1 - idx
            if idx == half_n:
                cur = ''.join(choosen) + mid_char + ''.join(choosen[::-1])
                if not tight or cur > target:
                    return cur
                return ''
            for c in sorted_char:
                if freg[c] == 0:
                    continue
                if tight:
                    if c < target[idx]:
                        continue
                freg[c] -= 1
                choosen.append(c)
                new_tight = tight and (c == target[idx])
                res = dp(idx + 1, new_tight)
                choosen.pop()
                freg[c] += 1
                if res:
                    return res
                if tight and c > target[idx]:
                    break
            return ''

        return dp(0, True)