def isPalidrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    return (string[0] == string[-1]) and isPalidrome(string[1:-1])


def longestPalindrome(s: str) -> str:
    k = 1
    n = len(s)
    max = s[0]
    for i in range(n):
        for j in range(i, n+1):
            if isPalidrome(s[i:j]):
                if j - i > k:
                    k = j - i
                    max = s[i:j]

    return max

print(isPalidrome("adxxca"))
print(longestPalindrome("babadxxcadsfafdaad"))
