from unittest import TestCase

from python_vervolg.examples2.mycode import do_something, Auto

def max_van_drie(a, b, c):
    return max(a, b, c)

def gemiddelde(getallen):
    if len(getallen) == 0:
        return 0
    else:
        return sum(getallen) / len(getallen)


class Test(TestCase):
    def test_do_something(self):
        self.assertEqual(do_something(0, 0), 0)
        self.assertEqual(do_something(1, 0), 1)
        self.assertEqual(do_something(2, 0), 2)
        # self.assertFalse(do_something(3,0),0)


class TestAuto(TestCase):
    def test_geef_gas(self):
        a = Auto(0)
        self.assertEqual(a.geefGas(10),10)
        self.assertEqual(a.geefGas(20),30)

class Test(TestCase):
    def test_gemiddelde(self):
        self.assertEqual(gemiddelde([2,4,6]),4)
        self.assertEqual(gemiddelde([]),0)