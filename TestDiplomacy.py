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
        a = diplomacy_start("A Madrid Hold")
        b = Army("A", "Madrid")
        self.assertEqual(b.name, a.name)
        self.assertEqual(b.city, a.city)

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB Madrid\nC London\n")

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
