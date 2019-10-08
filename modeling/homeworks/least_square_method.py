import matplotlib.pyplot as plt
import math

""" My first homework on modeling subject"""


def det(A, total=0):
    indices = list(range(len(A)))
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    for fc in indices:
        As = A.copy()
        As = As[1:]
        As = [As[i][0:fc] + As[i][fc + 1:] for i in range(len(As))]
        total += (-1) ** (fc % 2) * A[0][fc] * det(As)
    return total


def gaussian(a, b):
    """Solve the Linear algebraic equation systems with Gaussian method"""
    if det(a) == 0:
        print('det is equalt to : ', det(a))
        return "The system consists singular matrix therefore solution not exists or there are infinity solutions"
    for i in range(len(b)):
        k = i
        while a[k][i] == 0 and k + 1 != len(b):
            k += 1
        b[i], b[k] = b[k], b[i]
        a[i], a[k] = a[k], a[i]
        b[i] = [x / a[i][i] for x in b[i]]
        a[i] = [x / a[i][i] for x in a[i]]
        b[i + 1:] = [[x - a[j][i] * y for x, y in zip(b[j], b[i])] for j in range(i + 1, len(a[0]))]
        a[i + 1:] = [[x - a[j][i] * y for x, y in zip(a[j], a[i])] for j in range(i + 1, len(a[0]))]
    result = [0 for i in range(len(b))]
    for i in range(len(b) - 1, -1, -1):
        result[i] = b[i][0] - sum([a[i][j] * result[j] for j in range(len(a) - 1, -1, -1)])
    return result


# first problem of first homework
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
y = [0.000269819, 0.20966649, 0.405653264, 0.600161378, 0.808358635, 1.000460357, 1.206855043, 1.400662266, 1.603810939,
     1.807376137, 2.002681541]

a = [
    [sum([i ** 2 for i in x]), sum(x)],
    [sum(x), len(x)]
]

b = [[sum([i * j for i, j in zip(x, y)])], [sum(y)]]

# second problem of first homework
# x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
y = [
    5.007551402, 5.022739776, 5.084108155, 5.180491601, 5.325066589, 5.507693178, 5.725436069, 5.987606914, 6.289589143,
    6.628711888, 7.006814729]
# a = [
#     [sum([i ** 4 for i in x]), sum([i ** 3 for i in x]), sum([i ** 2 for i in x])],
#     [sum([i ** 3 for i in x]), sum([i ** 2 for i in x]), sum(x)],
#     [sum([i ** 2 for i in x]), sum(x), len(x)]
# ]
#
# b = [[sum([j * i ** 2 for i, j in zip(x, y)])], [sum([i * j for i, j in zip(x, y)])], [sum(y)]]

# third problem of first homework
# x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# initial_y = [1.011378034, 1.509673763, 2.2396243, 3.320296591, 4.95716554, 7.394593138, 11.02489662, 16.44550924,
#              24.53945915, 36.61225519, 54.60938299]
# y = [math.log(i, math.exp(1)) for i in initial_y]
# a = [
#     [sum([i ** 2 for i in x]), sum(x)],
#     [sum(x), len(x)]
# ]
#
# b = [[sum([i * j for i, j in zip(x, y)])], [sum(y)]]

solution = gaussian(a, b)  # the found x1, x2, ... , xn values
print(solution)
# first solution
plt.plot(x, y, ' bo', label='initial')
plt.plot(x, [solution[0] * i + solution[1] for i in x], label=r'${%f}x+{%f}$' % (solution[0], solution[1]))

# second solution
# plt.plot(x, y, ' o', label='initial')
# plt.plot(x, [solution[0] * i ** 2 + solution[1] * i + solution[2] for i in x], '-rx',
#          label=r'${%f}x^2+{%f}x+{%f}$' % (solution[0], solution[1], solution[2]))

# third
# plt.plot(x, initial_y, ' bo', label='initial')
# plt.plot(x, [math.exp(solution[1]) * math.exp(solution[0] * i) for i in x], '-rx',
#          label=r'${%f}e^{%sx}$' % (solution[1], {solution[0]}))
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('least square method')
plt.legend()
plt.show()
