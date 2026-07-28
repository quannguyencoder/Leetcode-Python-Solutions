# class Trie:
#     def __init__(self):
#         self.root={}

#     def insert(self, word: str) -> None:
#         node = self.root
#         for c in word:
#             node = node.setdefault(c, {})
#         node['end']=True


#     def search(self, word: str) -> bool:
#         node = self.root
#         for c in word:
#             if c not in node:
#                 return False
#             node = node[c]
#         return 'end' in node

#     def startsWith(self, prefix: str) -> bool:
#         node = self.root
#         for c in prefix:
#             if c not in node:
#                 return False
#             node = node[c]
#         return True

# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         rows, cols = len(board), len(board[0])
#         tree = Trie()
#         for word in words:
#             tree.insert(word)
#         found = set()
#         gone = set()

#         def helper(r, c, cur = ""):
#             gone.add((r, c))
#             cur += board[r][c]
#             if cur and not tree.startsWith(cur):
#                 gone.remove((r, c))
#                 return
#             if cur and tree.search(cur):
#                 found.add(cur)
#             for newR, newC in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
#                 if newR < 0 or newR >= rows or newC < 0 or newC >= cols or (newR, newC) in gone:
#                     continue
#                 gone.add((newR, newC))
#                 helper(newR, newC, cur)
#             gone.remove((r, c))
#         for r in range(rows):
#             for c in range(cols):
#                 helper(r, c)
#         return list(found)
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # 1. Xây dựng Trie trực tiếp bằng Dictionary
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            # Lưu trực tiếp từ hoàn chỉnh tại nút cuối thay vì cờ True/False
            node['$'] = word  

        rows, cols = len(board), len(board[0])
        found = []

        # 2. Hàm DFS truyền thẳng Nút Trie hiện tại (Tối ưu O(1) Prefix check)
        def dfs(r, c, parent_node):
            char = board[r][c]
            
            # Nếu ký tự không có trong nhánh Trie hiện tại -> Dừng (Cắt nhánh)
            if char not in parent_node:
                return
            
            curr_node = parent_node[char]
            
            # Nếu tìm thấy từ, thêm vào kết quả và xóa từ đó khỏi Trie để tránh tìm trùng
            if '$' in curr_node:
                found.append(curr_node['$'])
                del curr_node['$']
                
            # Đánh dấu đã thăm trực tiếp trên bảng (Tránh dùng Set tốn kém)
            board[r][c] = '#'
            
            # Duyệt 4 hướng liền kề
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, curr_node)
                    
            # Backtracking: Phục hồi lại ký tự gốc
            board[r][c] = char
            
            # TỐI ƯU SIÊU TỐC (PRUNING): 
            # Nếu nút hiện tại đã rỗng (tất cả các từ dưới nhánh này đã được tìm thấy),
            # Cắt bỏ hẳn nút này khỏi Trie để các luồng DFS khác không đi vào nữa.
            if not curr_node:
                del parent_node[char]

        # 3. Kích hoạt DFS từ mọi ô trên bảng
        for r in range(rows):
            for c in range(cols):
                # Chỉ bắt đầu DFS nếu ký tự ô đó là ký tự bắt đầu của một từ nào đó
                if board[r][c] in trie:
                    dfs(r, c, trie)
                    
        return found