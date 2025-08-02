class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        if start == destination:
            return 0
        elif start > destination:
            start, destination = destination, start
        direct = sum(distance[start:destination])
        return min(direct,total - direct)