import unittest
from Triangles_Ameya_Desai import classify_triangle
class TestContainer(unittest.TestCase):
    # unittest class

    def test_triangle(self):
        self.assertEqual(classify_triangle(5,5,5), "triangle is equilateral and not right angled")
        self.assertNotEqual(classify_triangle(4, 5, 5), "triangle is equilateral and not right angled")

        self.assertEqual(classify_triangle(5, 3, 4), "triangle is scalene and right angled")
        self.assertEqual(classify_triangle(5, 3, 2), "triangle is scalene and not right angled")
        self.assertEqual(classify_triangle(12, 13, 5), "triangle is scalene and right angled")

        self.assertEqual(classify_triangle(4, 4, 5), "triangle is isosceles and not right angled")
        self.assertEqual(classify_triangle(5, 5, 7.07), "triangle is isosceles and right angled")

        self.assertEqual(classify_triangle(4, 4, 500), "given triangle is invalid")



if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)