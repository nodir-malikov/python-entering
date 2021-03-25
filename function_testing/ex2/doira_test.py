import unittest
from function_testing.ex2.doira import getArea, getPerimeter


class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(5), 78.5, 1)
        # oxiridagi bir nuqtadan keyin o'nlik sonlardan qanchasini tekshirishni belbilab beradi
        self.assertAlmostEqual(getArea(15), 706.85, 1)

    def test_perimetr(self):
        self.assertAlmostEqual(getPerimeter(5), 31.400000000000002, 1)
        self.assertAlmostEqual(getPerimeter(15), 94.2, 1)


unittest.main()
