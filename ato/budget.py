import time
from collections import deque

class BudgetExceeded(Exception):
    pass

class RequestBudget:
    def __init__(self, max_total: int, max_per_minute: int):
        self.max_total = max_total
        self.max_per_minute = max_per_minute

        self.total_count = 0
        self.window = deque()  # timestamps of last requests (seconds)

    def _prune(self, now: float):
        # remove entries older than 60 seconds
        while self.window and now - self.window[0] > 60:
            self.window.popleft()

    def consume(self):
        now = time.time()
        self._prune(now)

        if self.total_count >= self.max_total:
            raise BudgetExceeded(
                f"total request budget exceeded ({self.total_count}/{self.max_total})"
            )

        if len(self.window) >= self.max_per_minute:
            raise BudgetExceeded(
                f"rate limit exceeded ({len(self.window)}/{self.max_per_minute} per minute)"
            )

        # commit
        self.total_count += 1
        self.window.append(now)
