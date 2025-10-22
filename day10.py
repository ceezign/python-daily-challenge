# Good morning! Here's your coding interview problem for today.
# This problem was asked by Amazon.
# There exists a staircase with N steps, and you can climb up either 1 or 2 steps
# at a time. Given N, write a function that returns the number of unique ways
# you can climb the staircase. The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could
# climb any number from a set of positive integers X? For example,
# if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


def climb_12(n: int) -> int:
    if n < 0:
        return 0
    if n <= 1:
        return 1
    a, b = 1, 1   # f(0), f(1)
    for _ in range(2, n + 1):
        a, b = b, a+b
    return b
print(climb_12(4))

def climb_X(n: int, X: set[int]) -> int:
    if n < 0:
        return 0
    if not X:
        return 0
    if any(x <= 0 for x in X):
        raise  ValueError("X must contain positive integers only.")

    ways = [0] * (n +1)
    ways[0] = 1
    for i in range(1, n + 1):
        total = 0
        for x in X:
            if i - x >= 0:
                total +=ways[i - x]
        ways[i] = total
    return ways[n]

print(climb_X(4, {1, 2}))
print(climb_X(6, {1, 3, 5}))
# Explanation for n=6,X={1,3,5} (order matters):
# counted by DP: ways[0]=1
# ways[1]=1
# ways[2]=1
# ways[3]=2   (1+1+1, 3)
# ways[4]=3   (1+1+1+1, 1+3, 3+1)
# ways[5]=5   (1+1+1+1+1, 1+1+3, 3+1+1, 5)
# ways[6]=8   (extend each by +1 where possible, or add +3 to ways[3], +5 to ways[1])





# Good morning! Here's your coding interview problem for today.
# This problem was asked by Amazon.
# Given an integer k and a string s, find the length of the longest substring
# that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k
# distinct characters is "bcb".


def longest_substring_k_distinct(s: str, k: int) -> int:
    if k == 0 or not s:
        return 0

    left = 0
    max_len = 0
    freq = {}

    for right, char in enumerate(s):
        # Add current character to frequency map
        freq[char] = freq.get(char, 0) + 1

        # if more than k distinct chars, shrink from left
        while len(freq) > k:
            left_char = s[left]
            freq[left_char] -= 1
            if freq[left_char] == 0:
                del freq[left_char]
            left += 1  # move left boundary

        # Update max lenght
        max_len = max(max_len, right - left + 1)
    return  max_len