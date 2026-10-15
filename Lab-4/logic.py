from collections import Counter


def feedback(code, guess):
    # Resolve exact matches first, then count partials only among the leftover
    # positions, so each code occurrence can contribute to feedback at most once.
    exact = sum(a == b for a, b in zip(code, guess))
    rest = [(a, b) for a, b in zip(code, guess) if a != b]
    partial = sum((Counter(a for a, _ in rest) & Counter(b for _, b in rest)).values())
    return exact, partial
