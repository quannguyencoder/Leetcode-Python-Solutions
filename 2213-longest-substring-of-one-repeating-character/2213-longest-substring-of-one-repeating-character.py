class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        

        tree_size = [0] * (4 * n + 1)
        tree_pref_c = [''] * (4 * n + 1)
        tree_pref_len = [0] * (4 * n + 1)
        tree_suff_c = [''] * (4 * n + 1)
        tree_suff_len = [0] * (4 * n + 1)
        tree_max_len = [0] * (4 * n + 1)
        
        def push_up(node):
            left = 2 * node
            right = 2 * node + 1
            
            tree_size[node] = tree_size[left] + tree_size[right]
            tree_pref_c[node] = tree_pref_c[left]
            tree_suff_c[node] = tree_suff_c[right]
            
            tree_max_len[node] = max(tree_max_len[left], tree_max_len[right])
            
            is_connected = (tree_suff_c[left] == tree_pref_c[right])
            
            if is_connected:
                tree_max_len[node] = max(tree_max_len[node], tree_suff_len[left] + tree_pref_len[right])
                
            tree_pref_len[node] = tree_pref_len[left]
            if is_connected and tree_pref_len[left] == tree_size[left]:
                tree_pref_len[node] += tree_pref_len[right]
                
            tree_suff_len[node] = tree_suff_len[right]
            if is_connected and tree_suff_len[right] == tree_size[right]:
                tree_suff_len[node] += tree_suff_len[left]

        def build(node, start, end):
            if start == end:
                c = s[start]
                tree_size[node] = 1
                tree_pref_c[node] = tree_suff_c[node] = c
                tree_pref_len[node] = tree_suff_len[node] = tree_max_len[node] = 1
                return
            
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            push_up(node) 
            
        def update(node, start, end, idx, val):
            if start == end:
                tree_pref_c[node] = tree_suff_c[node] = val
                return
            
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
                
            push_up(node)
        build(1, 0, n - 1)
        
        ans = []
        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            val = queryCharacters[i]
            update(1, 0, n - 1, idx, val)
            ans.append(tree_max_len[1])
            
        return ans