class Solution:
    def numSquares(self, n: int) -> int:
        queue = deque([(n, 0)])  # (remaining number, step count)
        visited = set()

        while queue:
            num, steps = queue.popleft()

            # Try all perfect squares <= num
            for i in range(1, int(math.sqrt(num)) + 1):
                next_num = num - i * i
                if next_num == 0:
                    return steps + 1  # Found the shortest path
                if next_num not in visited:
                    visited.add(next_num)
                    queue.append((next_num, steps + 1))

        return -1  # Should never reach here
