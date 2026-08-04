class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(room):
            visited.add(room)
            for cur_key in rooms[room]:
                if cur_key not in visited:
                    dfs(cur_key)
        dfs(0)
        return len(visited) == len(rooms)
        