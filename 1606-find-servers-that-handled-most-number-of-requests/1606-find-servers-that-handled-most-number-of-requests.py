class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        frequent = list(range(k)) 
        handled, busy = [], [] 
        for i, (t, d) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t: 
                heappush(frequent, i + (heappop(busy)[1] - i) % k)
            if frequent:  
                x = heappop(frequent) % k
                heappush(busy, (t + d, x))
                handled.append(x)
        return multimode(handled)