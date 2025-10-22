# Good morning! Here's your coding interview problem for today.
# This problem was asked by Microsoft.
# Given a dictionary of words and a string made up of those words (no spaces),
# return the original sentence in a list. If there is more than one possible
# reconstruction, return any of them. If there is no possible reconstruction,
# then return null.
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
# string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
# string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
# ['bedbath', 'and', 'beyond'].



def reconstruct_sentence(s: str, words: list) -> list | None:
    """
    Reconstruct s into a list of words from `words` (any valid reconstruction).
    Return None if no reconstruction exists.
    """
    word_set = set(words)                    # 0(1) membership  checks
    n = len(s)
    if n == 0:
        return []                            # empty string -> empty sentence

    # dp[i] = True means s[:i] can be formed
    dp = [False] * (n + 1)
    dp[0] = True                             # empty prefix is formable

    # back pointer: for position j store the index i where the last word started
    # and the actual word used to get to j
    prev_index = [-1] * (n + 1)
    word_used = [None] * (n + 1)

    max_word_len = max((len(w) for w in words), default=0)

    for i in range(n):
        if not dp[i]:
            continue
        # only check substrings up to max_word_len to save work
        end_limit = min(n, i + max_word_len)
        for j in range(i + 1, end_limit + 1):
            sub = s[i:j]
            if sub in word_set:
                if not dp[j]:            # store first found way to reach j
                    dp[j] = True
                    prev_index[j] = i
                    word_used[j] = sub

    if not dp[n]:
        return None                     # no was to form entire string

    # reconstruct the words by walking backwards from n
    result = []
    idx = n
    while idx > 0:
        result.append(word_used[idx])
        idx = prev_index[idx]
    result.reverse()
    return result

print(reconstruct_sentence("thequickbrownfox", ["quick", "brown", "the", "fox"]))
print(reconstruct_sentence("bedbathandbeyond", ["bed", "bath", "bedbath", "and", "beyond"]))


# Alternative Approach (recursive DFS + memo)

def reconstruct_dfs(s, words):
    word_set = set(words)
    memo = {}               # start index -> None or list or words from start_index

    def helper(i):
        if i == len(s):
            return []
        if i in memo:
            return memo[i]
        for j in range(i+1, len(s)+1):
            w = s[i:j]
            if w in word_set:
                rest = helper(j)
                if rest is not None:
                    memo[i] = [w] + rest
                    return memo[i]
        memo[i] = None
        return None
    return helper(0)

print(reconstruct_dfs("thequickbrownfox", ["quick", "brown", "the", "fox"]))
print(reconstruct_dfs("bedbathandbeyond", ["bed", "bath", "bedbath", "and", "beyond"]))










































