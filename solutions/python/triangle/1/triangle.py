def equilateral(sides):
    a, b, c = sides
    return a == b == c and a > 0


def isosceles(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a and (a == b or a == c or b == c)


def scalene(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a and a != b and b != c and a != c