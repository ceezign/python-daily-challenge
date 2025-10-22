# give the mapping a = 1, b = 1, ...z =26, and an encoded message, count the
# number of ways it can be decoded.
# For example, the message '111' would give 3,
# since it could be decoded as 'aaa', 'ka', and 'ak'.
# you can assume that the messages are decodable. for example, '001' is not allowed.


def num_decodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        # single digit decode
        if s[i-1] != '0':
            dp[i] += dp[i-1]

        # Two didit decode
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]

    return dp[n]

print(num_decodings("1111111"))