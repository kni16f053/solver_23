import math


def solve2(a, b, c, d=0):
    D = b * b - 4 * a * c
    if a != 0 and D == 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        return (1, x1)
    elif a != 0 and D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return (2, x1, x2)
    elif a == 0 and b == 0 and c != 0:
        return ('No roots')
    elif a == 0 and b != 0:
        return (1, -c / b)
    elif a != 0 and D < 0:
        return ('No real roots')
    elif a == 0 and b == 0 and c == 0:
        return ('Infinite roots')


def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def solve3(a, b, c, d):
    if a == 0:
        return solve2(b, c, d)
    else:
        Q = (a * a - 3 * b) / 9
        R = (2 * a * a * a - 9 * a * b + 27 * c) / 54
        S = Q * Q * Q - R * R
        if S > 0:
            phi = 1 / 3 * math.acos(R / (pow(Q, 1 / 3)))
            x1 = -2 * pow(Q, 1 / 2) * math.cos(phi) - (a / 3)
            x2 = -2 * pow(Q, 1 / 2) * math.cos(phi + 2 * math.pi / 3) - (a / 3)
            x3 = -2 * pow(Q, 1 / 2) * math.cos(phi - 2 * math.pi / 3) - (a / 3)
            return (3, x1, x2, x3)
        elif S < 0:
            if Q > 0:
                phi = math.acosh(abs(R) / pow(Q * Q * Q, 1 / 2)) / 3
                x1 = -2 * sgn(R) * pow(Q, 1 / 2) * math.cosh(phi) - (a / 3)
                return (1, x1)
            elif Q < 0:
                phi = math.asinh(abs(R) / pow(abs(Q * Q * Q), 1 / 2)) / 3
                x1 = -2 * sgn(R) * pow(abs(Q), 1 / 2) * math.sinh(phi) - (a / 3)
                return (1, x1)
            else:
                x1 = -1 * pow(c - a * a * a / 27, 1 / 3) - (a / 3)
                return (1, x1)
        else:
            x1 = -2 * pow(R, 1 / 3) - (a / 3)
            x2 = pow(R, 1 / 3) - (a / 3)
            return (2, x1, x2)


print(solve3(1, 1, 1, 1))