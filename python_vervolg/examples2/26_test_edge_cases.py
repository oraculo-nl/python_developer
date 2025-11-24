# 26_test_edge_cases.py
# Edge cases for boundaries and off by one errors.

def clamp(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x

def run_tests():
    assert clamp(5, 0, 10) == 5       # inside
    assert clamp(-1, 0, 10) == 0      # below
    assert clamp(11, 0, 10) == 10     # above
    assert clamp(0, 0, 10) == 0       # boundary low
    assert clamp(10, 0, 10) == 10     # boundary high
    print("OK: edge case tests passed")

if __name__ == "__main__":
    run_tests()
