def palindromo_longo(s):
    n = len(s)
    if n < 2:
        return s
    start = 0
    max_len = 1
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1):
        if s[i].isalpha() and s[i + 1].isalpha() and s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i].isalpha() and s[j].isalpha() and s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length
    return ''.join(c for c in s[start:start + max_len] if c.isalpha())
input_str = input("Digite uma palavra: ")
output_str = palindromo_longo(input_str)
print("O palíndromo mais longo é:", output_str)
