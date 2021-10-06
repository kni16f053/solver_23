import math


def solve2(a, b, c):
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

def get_cube_root(x):
    if x < 0:
        x = abs(x)
        cube_root = x**(1/3)*(-1)
    else:
        cube_root = x**(1/3)
    return cube_root


def solve3(a, b, c, d):
    if a == 0:
        return solve2(b, c, d)
    else:
        a_ = b / a
        b_ = c / a
        c_ = d / a
        Q = (3 * b_ - a_ * a_) / 9 #это  p / 3
        R = (2 * a_ * a_ * a_ - 9 * a_ * b_ + 27 * c_) / 54 #это q / 2 
        S = Q * Q * Q + R * R
        if S < 0:
            if R < 0:
                phi = math.atan(pow(-S, 1 / 2) / R)
                x1 = 2 * pow(-Q, 1 / 2) * math.cos(phi / 3) - (a_ / 3)
                x2 = 2 * pow(-Q, 1 / 2) * math.cos((phi / 3) + 2 * math.pi / 3) - (a_ / 3)
                x3 = 2 * pow(-Q, 1 / 2) * math.cos((phi / 3) + 4 * math.pi / 3) - (a_ / 3)
            elif R == 0:
                phi = math.pi / 2
                x1 = 2 * pow(-Q, 1 / 2) * math.cos(phi / 3) - (a_ / 3)
                x2 = 2 * pow(-Q, 1 / 2) * math.cos((phi / 3) + 2 * math.pi / 3) - (a_ / 3)
                x3 = 2 * pow(-Q, 1 / 2) * math.cos((phi / 3) + 4 * math.pi / 3) - (a_ / 3)
            else:
                phi = math.atan(pow(-S, 1 / 2) / -R) + math.pi
                x1 = 2 * pow(-Q, 1 / 2) * math.cos(phi / 3) - (a_ / 3)
                x2 = 2 * pow(-Q, 1 / 2) * math.cos((phi / 3) + 2 * math.pi / 3) - (a_ / 3)
                x3 = 2 * pow(-Q, 1 / 2) * math.cos((phi / 3) + 4 * math.pi / 3) - (a_ / 3)
            return (3, x1, x2, x3)
        elif S > 0:
            x1 = get_cube_root(-R + pow(S, 1 / 2)) + get_cube_root(-R - pow(S, 1 / 2)) - (a_ / 3)
            return (1, x1)
        else:
            if Q == 0:
                x1 = 0.0
                return (1, x1)
            else:
                x1 = 2 * get_cube_root(-R) - (a_ / 3)
                x2 = -get_cube_root(-R) - (a_ / 3)
                return (2, x1, x2)


print(solve3(1, -1, -2, 1)) # 3 корня
print(solve3(1, -10, -15, 4)) # 3 корня
print(solve3(1, -1, 3, 4)) # 1 корень
print(solve3(1, -1, 3, 4)) # 2 корня
print(solve3(0, 1, -3, 2)) # a = 0
print(solve3(0, 0, 0, 0)) # все 0
print(solve3(0, 0, 0, 1)) # 1 ноль
print(solve3(0, 0, 4, 1)) # 2 ноля
print(solve3(2, 0, 0, 0))