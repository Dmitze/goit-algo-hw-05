import timeit


def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore(text, pattern):
    if not pattern or not text:
        return -1
    
    shift_table = build_shift_table(pattern)
    i = 0
    
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    
    return -1


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp(text, pattern):
    if not pattern or not text:
        return -1
    
    lps = compute_lps(pattern)
    i = j = 0
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
        
        if j == len(pattern):
            return i - j
    
    return -1


def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1, modulus)
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp(text, pattern):
    if not pattern or not text or len(pattern) > len(text):
        return -1
    
    pattern_length = len(pattern)
    text_length = len(text)
    base = 256
    modulus = 101
    
    pattern_hash = polynomial_hash(pattern, base, modulus)
    text_hash = polynomial_hash(text[:pattern_length], base, modulus)
    h_multiplier = pow(base, pattern_length - 1, modulus)
    
    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash:
            if text[i:i + pattern_length] == pattern:
                return i
        
        if i < text_length - pattern_length:
            text_hash = (text_hash - ord(text[i]) * h_multiplier) % modulus
            text_hash = (text_hash * base + ord(text[i + pattern_length])) % modulus
            if text_hash < 0:
                text_hash += modulus
    
    return -1


f1 = open("article1.txt", encoding="utf-8").read()
f2 = open("article2.txt", encoding="utf-8").read()

real_word = "алгоритм"
fake_word = "xyzqwerty123"

print("Article 1:")
for name, func in [("Boyer-Moore", boyer_moore), ("KMP", kmp), ("Rabin-Karp", rabin_karp)]:
    t1 = timeit.timeit(lambda: func(f1, real_word), number=50)
    t2 = timeit.timeit(lambda: func(f1, fake_word), number=50)
    print(f"{name}: real={t1/50:.6f}s, fake={t2/50:.6f}s")

print("\nArticle 2:")
for name, func in [("Boyer-Moore", boyer_moore), ("KMP", kmp), ("Rabin-Karp", rabin_karp)]:
    t1 = timeit.timeit(lambda: func(f2, real_word), number=50)
    t2 = timeit.timeit(lambda: func(f2, fake_word), number=50)
    print(f"{name}: real={t1/50:.6f}s, fake={t2/50:.6f}s")
