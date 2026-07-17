from collections import deque

GLOBAL_MOVES = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)}


class GoalBasedAgent:

    def __init__(self):
        # Stores the calculated sequence of moves to reach the goal
        self.planned_path = []

    def _find_nearest_dirt_bfs(self, start_pos, grid):
        """Uses BFS search algorithm to find the shortest path to the closest

        dirt.
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque([[start_pos, []]])  # Format: [(current_row, current_col), [path_of_moves]]
        visited = {start_pos}

        while queue:
            (r, c), path = queue.popleft()

            # Goal Test: If we found dirt, return the path to get here
            if grid[r][c] == "D":
                return path

            # Explore future planning steps in all directions
            for move, (dr, dc) in GLOBAL_MOVES.items():
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] != "1"
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    queue.append([(nr, nc), path + [move]])

        return []  # No dirt reachable

    def act(self, pos, grid):
        r, c = pos

        # Rule 1: Always clean if currently standing on dirt
        if grid[r][c] == "D":
            self.planned_path = []  # Clear plan since goal is achieved
            return "CLEAN"

        # Rule 2: If we don't have a plan, search for the nearest goal
        if not self.planned_path:
            self.planned_path = self._find_nearest_dirt_bfs(pos, grid)

        # Rule 3: Follow the pre-planned sequence of actions
        if self.planned_path:
            return self.planned_path.pop(0)  # Take the next scheduled step

        return "STAY"


# --- Simulation Setup (Matching Your Template) ---

print("Enter number of rows:")
rows = int(input())
print("Enter number of columns:")
cols = int(input())

grid = []
print(
    f"Enter {rows} rows (space-separated values like '0 1 1' or 'D 0 1'):"
)
for _ in range(rows):
    grid.append(input().split())

print("Enter starting row index:")
start_r = int(input())
print("Enter starting column index:")
start_c = int(input())
pos = (start_r, start_c)

# Instantiate the new Goal-Based Agent
agent = GoalBasedAgent()

print("\n--- Simulation Results ---")
# Increased range to 10 to watch the long-term planning execute completely
for step in range(10):
    action = agent.act(pos, grid)
    print(f"Step {step+1} | Pos: {pos} -> Action: {action}")

    if action == "CLEAN":
        grid[pos[0]][pos[1]] = "0"
    elif action == "STAY":
        print("🎉 No more reachable dirt left or agent trapped!")
        break
    else:
        pos = (
            pos[0] + GLOBAL_MOVES[action][0],
            pos[1] + GLOBAL_MOVES[action][1],
        )
