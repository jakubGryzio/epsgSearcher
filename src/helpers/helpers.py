from collections import Counter


def most_common(lst):
    data = Counter(lst)
    if data:
        return max(lst, key=data.get)
