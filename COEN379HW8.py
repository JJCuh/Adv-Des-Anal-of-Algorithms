# Q2
def compute_Z(s):
    n = len(s)
    l = 0
    r = 1
    z = [0 for i in range(n)]

    for k in range(1, n):
        if r <= k:
            x = 0
            while k + x < n and s[x] == s[k+x]:
                x += 1
            z[k] = x
            l = k
            r = k + z[k]
        elif k + z[k-l] < r:
            z[k] = z[k-l]
        else:
            x = r - k
            while k + x < n and s[x] == s[k+x]:
                x += 1
            z[k] = x
            l = k
            r = k + z[k]

    return z

def compute_N(s):
    n = len(s)
    t = ''.join(reversed(s)) # reverses string s
    z = compute_Z(t)
    a = list(reversed(z)) # reverses z-list

    return a

print(compute_N("ABAABAAAB")) # test

# Q3
def longestPreSuf(s, t):
    st = s + t
    z = compute_Z(st)
    n = len(z)

    a = 0
    for k in range(n):
        val = z[k]
        if (k + val == n):
            if (val <= min(len(s), len(t)) and val > a):
                a = val
    
    return s[:a]

print(longestPreSuf("abadfw", "gesaba")) # test