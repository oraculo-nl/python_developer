from testen1 import tel_op

def test_tel_op():
    assert tel_op(1, 2) == 3
    assert tel_op(-1, 2) == 1
    assert tel_op(-11, -2) == -13
    assert tel_op(0, 2) == 2