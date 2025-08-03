class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:

        positions = [pos for pos, _ in fruits]
        prefix = [0]
        for _, amount in fruits:
            prefix.append(prefix[-1] + amount)
        
        def range_sum(left: int, right: int) -> int:
            return prefix[right] - prefix[left]

        ans = 0


        for x in range(len(fruits)):
            left_pos = fruits[x][0]
            if left_pos > startPos:
                break
            steps_left = startPos - left_pos
            remain = k - 2 * steps_left
            if remain < 0:
                continue
            right_limit = startPos + remain
            y = bisect_right(positions, right_limit)
            ans = max(ans, range_sum(x, y))


        for y in range(len(fruits)):
            right_pos = fruits[y][0]
            if right_pos < startPos:
                continue
            steps_right = right_pos - startPos
            remain = k - 2 * steps_right
            if remain < 0:
                continue
            left_limit = startPos - remain
            x = bisect_left(positions, left_limit)
            ans = max(ans, range_sum(x, y + 1))

        left_limit = startPos - k
        i = bisect_left(positions, left_limit)
        j = bisect_right(positions, startPos)
        ans = max(ans, range_sum(i, j))


        right_limit = startPos + k
        i = bisect_left(positions, startPos)
        j = bisect_right(positions, right_limit)
        ans = max(ans, range_sum(i, j))

        return ans