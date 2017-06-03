def is_max_heap(a):
    """ DP step of finding palindrome subtring with max length """
    
    if i > j:  # over
        return ""
    
    if i == j:  # same letter
        return s[i]
    
    if s[i] == s[j]:
        return s[i] + max_substr_pal_dp(s, i + 1, j - 1) + s[j] # possible palindrome
    else:
        s1 = max_substr_pal_dp(s, i, j - 1)  # try all alternatives
        s2 = max_substr_pal_dp(s, i + 1, j)
        if len(s1) > len(s2):
            return s1
        else:
            return s2


def max_substr_pal(s):
    """ Finds palindrome subtring with max length """
    
    i = 0  # index of start of such substr
    j = len(s) - 1  # index of end of such substr
    maxs = ""  # such subtr
    print(max_substr_pal_dp(s, i, j))


if __name__ == '__main__':
    max_substr_pal("colonno")  # onno
    max_substr_pal("colonna")  # olo
