def classify_triangle(a,b,c):
    """Check the triangle"""

print("Input lengths of the triangle sides: ")
print("Enter values for sides of the triangle: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a == b == c:
    print("Equilateral Triangle")
elif a==b or b==c or c==a:
    print("Isosceles Triangle")
elif a*a + b*b == c*c:
    print("Right Angled Triangle")
elif a!=b==c:
    print("Scalene Triangle")