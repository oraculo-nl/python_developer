# 24_test_floats_tolerance.py
# Testing floating point with a tolerance. No classes used.

def mean(xs):
    if not xs:
        return None
    return sum(xs) / float(len(xs))

def approx_equal(a, b, tol=1e-9):
    if a is None or b is None:
        return a is b
    return abs(a - b) <= tol

def run_tests():
    assert approx_equal(mean([2, 4, 6]), 4.0)
    assert mean([]) is None
    # A case that can suffer from float rounding
    m = mean([0.1, 0.1, 0.1, 0.3])
    assert approx_equal(m, 0.15)
    print("OK: float tolerance tests passed")

if __name__ == "__main__":
    run_tests()
