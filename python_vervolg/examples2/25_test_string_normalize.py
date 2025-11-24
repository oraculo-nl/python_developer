# 25_test_string_normalize.py
# Testing a small string normalization helper.

def normalize_name(s):
    # strip, lower, collapse inner spaces to single space
    parts = s.strip().lower().split()
    return " ".join(parts)

def run_tests():
    assert normalize_name("  Alice  ") == "alice"
    assert normalize_name("Bob   van  Dijk") == "bob van dijk"
    assert normalize_name("  ") == ""
    print("OK: string normalize tests passed")

if __name__ == "__main__":
    run_tests()
