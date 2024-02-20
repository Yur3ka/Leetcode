def myAtoi( s: str) -> int:
    s = s.lstrip()
    negative = False
    string_int = ""
    max_int = 2 ** 31 - 1
    min_int = -2 * 31
    if s[0] in ["-", "+"]:
        if s[0] == "-":
            negative = True
        s = s[1:]
    for char in s:
        if char not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            break
        else:
            string_int += char
    if len(string_int) == 0:
        return 0
    result = int(string_int)
    if negative:
        result *= -1
    if result > max_int:
        return max_int
    elif result < min_int:
        return min_int
    else:
        return result

print(myAtoi("-3514251452345245"))