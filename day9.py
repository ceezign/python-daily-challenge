# Good morning! Here's your coding interview problem for today.
# This problem was asked by Airbnb.
# Given a list of integers, write a function that returns the largest sum of
# non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.
import time


def largest_non_adjacent_sum(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return max(0, nums[0])  # handle negative case

    #  initialize
    dp = [0] * len(nums)
    dp[0] = max(0, nums[0])
    dp[1] = max(dp[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    return dp[-1]

#Example
print(largest_non_adjacent_sum([2, 4, 6, 2, 5]))
print(largest_non_adjacent_sum([5, 1, 1, 5]))
print(largest_non_adjacent_sum([-1, -2, -3]))






#Good morning! Here's your coding interview problem for today.
#This problem was asked by Apple.
#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import time
def scheduler(f, n):
    time.sleep(n / 1000)
    f()

def say_hello():
    print("hello world")

scheduler(say_hello, 2000 )

# Good morning! Here's your coding interview problem for today.
# This problem was asked by Twitter.
# Implement an autocomplete system. That is, given a query string s and a set
# of all possible query strings, return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class AutocompleteSystem:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def _dfs(self, node, prefix, results):
        if node.is_end:
            results.append(prefix)
        for ch, child in node.children.items():
            self._dfs(child, prefix + ch, results)

    def autoComplete(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []  # no matches
            node = node.children[ch]

        results = []
        self._dfs(node, prefix, results)
        return results

words = ["dogs", "deer", "deal"]
system = AutocompleteSystem(words)

print(system.autoComplete("de")) # [deer, deal]
print(system.autoComplete("do"))  # [dog]
print(system.autoComplete("cat"))  # []
