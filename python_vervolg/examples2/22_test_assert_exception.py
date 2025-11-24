# 22_test_assert_exception.py
# Testing exceptions using try/except and assert.

def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b

def run_tests():
    assert divide(10, 2) == 5
    # Check that ValueError is raised for division by zero
    try:
        divide(1, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError as e:
        assert "zero" in str(e)
    print("OK: exception tests passed")

if __name__ == "__main__":
    run_tests()
