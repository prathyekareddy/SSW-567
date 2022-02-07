import unittest

def classify_triangle(a,b,c):
    """Check the triangle"""
    print("Input lengths of the triangle sides: ")
    if a == b == c:
        return("Equilateral Triangle")
    elif a==b or b==c or c==a:
        return("Isosceles Triangle")
    elif a*a + b*b == c*c:
        return("Right Angled Triangle")
    elif a!=b!=c:
        return("Scalene Triangle")
class Test_Triangle(unittest.TestCase):
    def test_Equilateral_Triangle(self):
        self.assertEqual(classify_triangle(3,3,3),"Equilateral Triangle") 
        self.assertEqual(classify_triangle(3,3,7),"Equilateral Triangle") 
        self.assertEqual(classify_triangle(4,3,3),"Equilateral Triangle")  
    def test_Isosceles_Triangle(self):  
        self.assertEqual(classify_triangle(2,4,2),"Isosceles Triangle")
        self.assertEqual(classify_triangle(2,4,7),"Isosceles Triangle")
        self.assertEqual(classify_triangle(5,4,2),"Isosceles Triangle")
    def test_Right_Angled_Triangle(self): 
        self.assertEqual(classify_triangle(3,4,5),"Right Angled Triangle")
        self.assertEqual(classify_triangle(9,4,5),"Right Angled Triangle")
        self.assertEqual(classify_triangle(3,4,3),"Right Angled Triangle")
    def test_Scalene_Triangle(self):
        self.assertEqual(classify_triangle(2,5,4),"Scalene Triangle")
        self.assertEqual(classify_triangle(8,8,4),"Scalene Triangle")
        self.assertEqual(classify_triangle(4,5,4),"Scalene Triangle")
if __name__ == '__main__':
    unittest.main()