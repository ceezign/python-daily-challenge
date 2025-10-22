# Good morning! Here's your coding interview problem for today.
# This problem was asked by Twitter.
# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be
# smaller than or equal to N.
# You should be as efficient with time and space as possible.
#

class OrderLog:
    """Fixed-capacity log of the last N order_ids using a circular buffer.
    record(order_id): 0(1) - write at the current head and advance.
    get_last(i): 0(1) - return the i-th most recent (i=1 means latest).
    """
    __slot__ = ("_buf", "_n", "_head", "_count")

    def __init__(self, N: int):
        if N <= 0:
            raise ValueError("N must be positive")
        self._buf = [None] * N       # fixed-size storage
        self._n = N                  # capacity
        self._head = 0               # next write position
        self._count = 0              # how many item we have actually written (<=N)

    def record(self, order_id):
        """Add an order_id to the log. """
        self._buf[self._head] = order_id     # write at head
        self._head = (self._head + 1) % self._n  # advance head modulo N
        if self._count < self._n:
            self._count += 1

    def get_last(self, i: int):
        """
        get the i-th last element (1-based: i=1 is the most recent).
        Raises IndexError if i is out of range of items we actually have.
        """
        if not 1 <= i <= self._n:
            raise IndexError("i must be between 1 and N inclusive")
        if i > self._count:
            raise  IndexError(f"Only {self._count} items recorded so far")
        # The most item is just before _head
        # i-th last is (_head - i) modulo N
        idx = (self._head - 1) % self._n
        return self._buf[idx]

if __name__ == "__main__":
    log = OrderLog(3)
    log.record("A")          # buffer: [A, None, None], head=1
    log.record("B")          # buffer: [A, B, None], head=2
    print(log.get_last(1))   # -> B
    log.record("C")          # buffer: [A, B, C], head=0
    print(log.get_last(2))   # -> B
    log.record("D")          # overwrites oldest (A): buffer: [D, B, C], head=1
    print(log.get_last(3))   # -> C (order is D (latest), c, B






# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# Given an array of integers and a number k, where 1 <= k <= length of the array,
# compute the maximum values of each subarray of length k.
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place
# and you do not need to store the results. You can simply print them out as you compute them.
#

from collections import deque

def print_window_max(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("k must be between 1 and len(arr)")
    dq = deque()       # will store indices; values are in decreasing order in dq

    # 1) pre-fill with the first k elements
    for i in range(k):
        # pop smaller elements from the back - they cant be maxima anymore
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        dq.append(i)

    # 2) First window max is at the front
    print(arr[dq[0]])

    # 3) Slide he window from i = k to n-1
    for i in range(k, len(arr)):
        # remove indices that fall out of the window (left side)
        while dq and dq[0] <= i -k:
            dq.popleft()

        # Maintain decreasing order: remove smaller/equal values from the back
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()

        dq.append(i)

        # the front holds the current windows maximum
        print(arr[dq[0]])

print(print_window_max([10, 5, 2, 7, 8, 7], k = 2))


# Good morning! Here's your coding interview problem for today.
# This problem was asked by Facebook.
# A builder is looking to build a row of N houses that can be of K different colors.
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
# Given an N by K matrix where the nth row and kth column represents the cost to
# build the nth house with kth color, return the minimum cost which achieves this goal.
#

def min_paint_cost(costs):
    """
    costs: N x K matrix, costs[i][c] = cost to paint house i with color c
    Returns minimal total cost subject to adjacent houses having different colors.
    Time: O(N*K), Space: O(1) extra.
    """
    if not costs:
        return 0
    n, k = len(costs), len(costs[0])
    if k == 0:
        return 0
    if k == 1:
        # Only valid if there's at most one house; otherwise impossible under the constraint.
        return costs[0][0] if n == 1 else float("inf")

    # prev row's best and second-best totals and their color indices
    prev_min1 = 0        # best total up to previous row
    prev_c1 = -1         # color that achieved prev_min1
    prev_min2 = 0        # second best total up to previous row
    prev_c2 = -1         # color that achieved prev_min2

    for i in range(n):
        cur_min1 = float("inf"); cur_c1 = -1
        cur_min2 = float("inf"); cur_c2 = -1

        for c in range(k):
            base = prev_min1 if c != prev_c1 else prev_min2
            total = costs[i][c] + base

            # Update current row's best and second-best
            if total < cur_min1:
                cur_min2, cur_c2 = cur_min1, cur_c1
                cur_min1, cur_c1 = total, c
            elif total < cur_min2:
                cur_min2, cur_c2 = total, c

        prev_min1, prev_c1 = cur_min1, cur_c1
        prev_min2, prev_c2 = cur_min2, cur_c2

    return prev_min1

costs = [
    [1, 5, 3],
    [2, 9, 4],
    [3, 1, 6],
]
print(min_paint_cost(costs))