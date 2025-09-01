from heapq import heappop, heappush
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def delta(pass_count, total_count):
            return (pass_count + 1) / (total_count + 1) - pass_count / total_count
        heap = []
        for pass_count, total_count in classes:
            heappush(heap, (-delta(pass_count, total_count), pass_count,total_count))
        for _ in range(extraStudents):
            max_delta, pass_count, total_count = heappop(heap)
            pass_count += 1
            total_count += 1
            heappush(heap, (-delta(pass_count, total_count), pass_count, total_count))
        return sum(pass_count / total_count for _, pass_count, total_count in heap) / len(classes)