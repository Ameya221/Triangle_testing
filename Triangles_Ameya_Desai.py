""Code to classify triangle type"""
def classify_triangle(side1, side2, side3):
    """ this function determines type of triangle"""
    if side1 > side2+side3 or side2 > side1+side3 or side3 > side1+side2:
        return "given triangle is invalid"
    ang = "not right angled"
    if round(max(side1, side2, side3)**2) == side1**2 + side2**2 or round(max(side1, side2, side3)**2) == side1**2 + side3**2 or round(max(side1, side2, side3)**2) == side3**2 + side2**2:
        ang = "right angled"

    if side1 == side2 == side3:
        typ = "equilateral"
    elif side1 == side2 or side2 == side3 or side3 == side1:
        typ = "isosceles"
    else:
        typ = "scalene"

    return f"triangle is {typ} and {ang}"
