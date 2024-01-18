def equilateral(sides):
    return all(x > 0 for x in sides) and len(set(sides)) == 1


def isosceles(sides):
    return (len(set(sides)) == 2 and valid_triangle(sides)) or equilateral(sides)


def scalene(sides):
    return valid_triangle(sides) and len(set(sides)) == 3


def valid_triangle(sides):
    return all(x > 0 for x in sides) and (
        sides[0] <= sides[1] + sides[2]
        and sides[1] <= sides[0] + sides[2]
        and sides[2] <= sides[0] + sides[1]
    )
