"""Wildcard Matching ('?' and '*') using DP and Greedy."""

def is_match_wildcard(s: str, p: str) -> bool:
    s_ptr = p_ptr = 0
    star_idx = -1
    s_temp = -1

    while s_ptr < len(s):
        if p_ptr < len(p) and p[p_ptr] in {s[s_ptr], "?"}:
            s_ptr += 1
            p_ptr += 1
        elif p_ptr < len(p) and p[p_ptr] == "*":
            star_idx = p_ptr
            s_temp = s_ptr
            p_ptr += 1
        elif star_idx != -1:
            p_ptr = star_idx + 1
            s_temp += 1
            s_ptr = s_temp
        else:
            return False

    while p_ptr < len(p) and p[p_ptr] == "*":
        p_ptr += 1

    return p_ptr == len(p)

if __name__ == "__main__":
    print("Wildcard 'acdcb' against 'a*c?b':", is_match_wildcard("acdcb", "a*c?b"))
    print("Wildcard 'adceb' against '*a*b':", is_match_wildcard("adceb", "*a*b"))
