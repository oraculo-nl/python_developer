# 28_test_randomized_checks.py
# Simple randomized checks (property-like) without external libs.

import random

def reverse_twice(xs):
    ys = list(xs)
    ys.reverse()
    ys.reverse()
    return ys

def run_tests():
    random.seed(0)
    for _ in range(200):
        n = random.randint(0, 20)
        xs = [random.randint(-50, 50) for _ in range(n)]
        ys = reverse_twice(xs)
        assert ys == xs, "reversing twice should yield original sequence"
    print("OK: randomized checks passed")

if __name__ == "__main__":
    run_tests()
