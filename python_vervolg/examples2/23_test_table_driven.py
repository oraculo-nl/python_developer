# 23_test_table_driven.py
# Table driven tests in plain Python with assert.

def max_of_three(a, b, c):
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m

CASES = [
    ((3, 2, 1), 3),
    ((-5, -2, -9), -2),
    ((0, 0, 0), 0),
    ((7, 9, 8), 9),
    ((1.5, 1.2, 1.3), 1.5),
]

def run_tests():
    for args, expected in CASES:
        got = max_of_three(*args)
        assert got == expected, f"max_of_three{args} -> {got}, expected {expected}"
    print("OK: table driven tests passed")

if __name__ == "__main__":
    run_tests()
