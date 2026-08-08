class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        seen = {}
        for cur in regions:
            root = cur[0]
            if root not in seen:
                seen[root] = root
            for child in cur[1:]:
                seen[child] = root
        root = seen[region1]
        fa1 = {region1}
        while True:
            fa1.add(root)
            if root == seen[root]:
                break
            root = seen[root]
        root = region2
        while True:
            if root in fa1:
                return root
            root = seen[root]
        