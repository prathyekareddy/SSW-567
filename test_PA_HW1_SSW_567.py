def classify_triangle(a,b,c):
    """Check the triangle"""

print("Input lengths of the triangle sides: ")
print("Enter values for sides of the triangle: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

def test_Equilateral_Triangle(a,b,c):
    assert a == b == c  
def test_Isosceles_Triangle(a,b,c):  
    assert a==b or b==c or c==a  
def test_Right_Angled_Triangle(a,b,c): 
    assert a*a + b*b == c*c
def test_Scalene_Triangle(a,b,c):
    assert a!=b!=c

if a == b == c:
    print("Equilateral Triangle")
elif a==b or b==c or c==a:
    print("Isosceles Triangle")
elif a*a + b*b == c*c:
    print("Right Angled Triangle")
elif a!=b!=c:
    print("Scalene Triangle")
    