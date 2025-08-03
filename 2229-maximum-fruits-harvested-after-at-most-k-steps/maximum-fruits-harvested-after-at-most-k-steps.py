class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:

        ans = 0
        positions = [pos for pos, _ in fruits]

        # Chèn startPos nếu chưa có, để tính prefix đúng tại vị trí đó
        curr = bisect_left(positions, startPos)
        if curr >= len(fruits) or fruits[curr][0] != startPos:
            fruits.insert(curr, [startPos, 0])
            positions.insert(curr, startPos)

        # Tính prefix sum số trái cây
        pre_sum = [0]
        s = 0
        for _, amount in fruits:
            s += amount
            pre_sum.append(s)

        # Tìm giới hạn trái và phải trong phạm vi k bước
        left_idx = bisect_left(positions, startPos - k)
        right_idx = bisect_right(positions, startPos + k)

        # Đi trái trước rồi phải
        for i in range(left_idx, curr + 1):
            steps_left = startPos - positions[i]
            remain_right = k - steps_left * 2
            if remain_right < 0:
                r_idx = curr
            else:
                r_idx = bisect_right(positions, startPos + remain_right)
            temp_fruits = pre_sum[r_idx] - pre_sum[i]
            ans = max(ans, temp_fruits)

        # Đi phải trước rồi trái
        for i in range(curr, right_idx):
            steps_right = positions[i] - startPos
            remain_left = k - steps_right * 2
            if remain_left < 0:
                l_idx = curr
            else:
                l_idx = bisect_left(positions, startPos - remain_left)
            temp_fruits = pre_sum[i + 1] - pre_sum[l_idx]
            ans = max(ans, temp_fruits)

        return ans
