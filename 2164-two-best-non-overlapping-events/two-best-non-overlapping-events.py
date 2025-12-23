class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        from bisect import bisect_left
        # Sort events by their end times
        events.sort(key=lambda x: x[1])
        
        # Precompute maximum values for a single event
        max_single = 0
        max_value = 0
        event_ends = []
        dp = []

        for event in events:
            start, end, value = event
            # Binary search to find the latest event that ends before this one starts
            idx = bisect_left(event_ends, start) - 1
            best_non_overlap = dp[idx] if idx >= 0 else 0
            
            # Compute the best value using the current event
            max_value = max(max_value, value + best_non_overlap)
            
            # Update the rolling max for a single event
            max_single = max(max_single, value)
            
            # Keep track of end times and max values for dp
            event_ends.append(end)
            dp.append(max_single)

        return max_value


