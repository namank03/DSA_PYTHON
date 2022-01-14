from collections import Counter

N = 5
words = ['act', 'god', 'cat', 'dog', 'tac']


def anagrams(words):
    g = {}
    for word in words:
        g.setdefault(frozenset(Counter(word).items()), []).append(word)
    return g.values()


res = anagrams(words)

print(f'res -> {res}')
