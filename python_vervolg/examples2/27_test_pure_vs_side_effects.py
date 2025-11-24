# 27_test_pure_vs_side_effects.py
# Favor testing pure functions. No file IO or classes.

def to_prices(lines):
    # lines like: "2024-01-01,100.50"
    prices = []
    for ln in lines:
        ln = ln.strip()
        if not ln:
            continue
        date_s, price_s = ln.split(",")
        prices.append(float(price_s))
    return prices

def total(prices):
    return sum(prices)

def run_tests():
    lines = [
        "2024-01-01,100.50",
        "2024-01-02,  99.50",
        "2024-01-03, 101.00",
        "",
    ]
    ps = to_prices(lines)
    assert ps == [100.50, 99.50, 101.00]
    assert total(ps) == 301.0
    print("OK: pure function tests passed")

if __name__ == "__main__":
    run_tests()
