#input and Output:
# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

# The lock initially starts at '0000', a string representing the state of the 4 wheels.

# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

# Example 1:

# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation: 
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
# Example 2:

# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
# Example 3:

# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# Output: -1
# Explanation: We cannot reach the target without getting stuck.
 

# Constraints:

# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target will not be in the list deadends.
# target and deadends[i] consist of digits only.

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)  # Convert to a set for quick lookup
        start = "0000"

        # If the start is a deadend, return -1
        if start in deadends:
            return -1

        # BFS setup
        queue = deque([(start, 0)])  # (current combination, moves)
        visited = set([start])  # Keep track of visited combinations

        # Function to generate all possible moves from a state
        def get_neighbors(combo):
            neighbors = []
            for i in range(4):  # There are 4 wheels
                digit = int(combo[i])
                for diff in [-1, 1]:  # Move the wheel forward or backward
                    new_digit = (digit + diff) % 10  # Wrap around 0-9
                    new_combo = combo[:i] + str(new_digit) + combo[i+1:]
                    neighbors.append(new_combo)
            return neighbors

        # BFS traversal
        while queue:
            current, moves = queue.popleft()

            # If we reach the target, return the number of moves
            if current == target:
                return moves

            # Explore all possible next moves
            for neighbor in get_neighbors(current):
                if neighbor not in visited and neighbor not in deadends:
                    queue.append((neighbor, moves + 1))
                    visited.add(neighbor)

        return -1  # If we exhaust all options without finding the target
