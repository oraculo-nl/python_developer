# 21_test_assert_basic.py
# Basic asserts for a small function. No classes, only functions and assert statements.

def add(a, b):
    return a + b

def run_tests():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("OK: basic add tests passed")

if __name__ == "__main__":
    run_tests()
