# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Diplomacy import Army, diplomacy_start, diplomacy_action, diplomacy_support, diplomacy_outcome, diplomacy_solve

# -----------
# TestDiplomacy
# -----------


class TestDiplomacy (TestCase):

    # -----
    # start
    # -----

    def test_start(self):
        a = diplomacy_start("A Frisco Hold")
        self.assertEqual("A", a.name)
        self.assertEqual("Frisco", a.city)
    
    def test_start2(self):
        a = diplomacy_start("B Tulsa Move DC")
        self.assertEqual("B", a.name)
        self.assertEqual("DC", a.city)
    
    def test_start2(self):
        a = diplomacy_start("Z Orlando Support G")
        self.assertEqual("Z", a.name)
        self.assertEqual("Orlando", a.city)
        self.assertEqual("G", a.target)

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("A Dallas Hold\nB Austin Move Dallas\nC Houston Support B\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB Dallas\nC Houston\n")
    
    def test_solve2(self):
        r = StringIO("C Houston Support B\nB Austin Move Dallas\nA Dallas Hold\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB Dallas\nC Houston\n")
    
    def test_solve2(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB [dead]\nC [dead]\nD Paris\nE Austin\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
$ coverage run --branch TestDiplomacy.py >  TestDiplomacy.out 2>&1


$ cat TestDiplomacy.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


$ coverage report -m                   >> TestDiplomacy.out



$ cat TestDiplomacy.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Diplomacy.py          12      0      2      0   100%
TestDiplomacy.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
