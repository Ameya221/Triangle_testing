def classify_triangle(a,b,c):
    if a > b+c or b > a+c or c> a+b:
        return "given triangle is invalid"
    ang = "not right angled"
    if round(max(a,b,c)**2) == a**2 + b**2 or round(max(a,b,c)**2) == a**2 + c**2 or round(max(a,b,c)**2) == c**2 + b**2:
        ang = "right angled"

    if a == b ==c:
        typ = "equilateral"
    elif a == b or b == c or c == a:
        typ = "isosceles"
    else:
        typ = "scalene"

    return f"triangle is {typ} and {ang}"


print(classify_triangle(4,4,5))