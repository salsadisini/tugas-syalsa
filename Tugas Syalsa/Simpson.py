import math

# Function to calculate velocity
def velocity(t, g, m, c):
    return g * m / c * (1 - math.exp(-c / m * t))

# Simpson 13 function
def Simp13(h, f0, f1, f2):
    return 2 * h * (f0 + 4 * f1 + f2) / 6

# Simpson 38 function
def Simp38(h, f0, f1, f2, f3):
    return 3 * h * (f0 + 3 * (f1 + f2) + f3) / 8

# Simpson 13 M function
def Simp13m(h, n, f):
    sum_result = f[0]
    for i in range(1, n-1, 2):
        sum_result = sum_result + 4 * f[i] + 2 * f[i+1]
    sum_result = sum_result + 4 * f[n-1] + f[n-2]
    return h * sum_result / 3

# Simpson Int function
def SimpInt(a, b, n, g, m, c):
    h = (b - a) / n
    f_values = [g * m / c * (1 - math.exp(-c / m * (a + i * h))) for i in range(n+1)]
    sum_result = 0

    if n == 1:
        sum_result = Simp13(h, f_values[0], f_values[1], f_values[2])
    else:
        m = n
        odd = n / 2 - int(n / 2)
        if odd > 0 and n > 1:
            sum_result = sum_result + Simp38(h, f_values[n-3], f_values[n-2], f_values[n-1], f_values[n])
            m = n - 3
        if m > 1:
            sum_result = sum_result + Simp13m(h, m, f_values)

    return sum_result

# Known parameters
g = 9.8  # gravitational constant (m/s^2)
m = 68.1  # mass of the parachutist (kg)
c = 12.5  # drag coefficient (kg/s)

# Analytical result for comparison
analytical_result = 289.43515

# Testing with different numbers of segments
segment_counts = [2, 5, 10, 100, 1000]
for segments in segment_counts:
    result = SimpInt(0, 10, segments, g, m, c)
    print(f"Segments: {segments}, Result: {result}, Error: {abs(result - analytical_result)}")