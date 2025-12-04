import timeit


def search1(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        match = True
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i
    return -1


def search2(text, pattern):
    bad = {}
    for i in range(len(pattern)):
        bad[pattern[i]] = i
    
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        shift = j - bad.get(text[i + j], -1)
        i += shift
    return -1


def search3(text, pattern):
    q = 101
    d = 256
    
    p = 0
    t = 0
    for i in range(len(pattern)):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    
    for i in range(len(text) - len(pattern) + 1):
        if p == t:
            if text[i:i + len(pattern)] == pattern:
                return i
        
        if i < len(text) - len(pattern):
            h = pow(d, len(pattern) - 1, q)
            t = (d * (t - ord(text[i]) * h) + ord(text[i + len(pattern)])) % q
    
    return -1


f1 = open("article1.txt", encoding="utf-8").read()
f2 = open("article2.txt", encoding="utf-8").read()

word = "алгоритм"
fake = "xyzqwerty123"

print("Article 1:")
for name, func in [("Linear", search1), ("Boyer-Moore", search2), ("Hash", search3)]:
    t1 = timeit.timeit(lambda: func(f1, word), number=50)
    t2 = timeit.timeit(lambda: func(f1, fake), number=50)
    print(f"{name}: real={t1/50:.6f}s, fake={t2/50:.6f}s")

print("\nArticle 2:")
for name, func in [("Linear", search1), ("Boyer-Moore", search2), ("Hash", search3)]:
    t1 = timeit.timeit(lambda: func(f2, word), number=50)
    t2 = timeit.timeit(lambda: func(f2, fake), number=50)
    print(f"{name}: real={t1/50:.6f}s, fake={t2/50:.6f}s")
