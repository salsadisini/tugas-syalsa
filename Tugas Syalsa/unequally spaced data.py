import math

def v(t):
    g = 9.8  # gravitational constant (m/s^2)
    m = 68.1  # mass of the parachutist (kg)
    c = 12.5  # drag coefficient (kg/s)

    return g * m / c * (1 - math.exp(-c / m * t))

def Trap(h, f0, f1):
    return h / 2 * (f0 + f1)

def Simp13(h, f0, f1, f2):
    return h / 3 * (f0 + 4 * f1 + f2)

def Simp38(h, f0, f1, f2, f3):
    return 3 * h / 8 * (f0 + 3 * (f1 + f2) + f3)

def Uneven(n, x, f):
    h = x[1] - x[0]
    k = 1
    summation = 0

    for j in range(1, n):
        hf = x[j + 1] - x[j]

        if abs(h - hf) < 0.000001:
            if k == 3:
                summation += Simp13(h, f[j - 3], f[j - 2], f[j - 1])
                k -= 1
            else:
                k += 1
        else:
            if k == 1:
                summation += Trap(h, f[j - 1], f[j])
            else:
                if k == 2:
                    summation += Simp13(h, f[j - 2], f[j - 1], f[j])
                else:
                    summation += Simp38(h, f[j - 3], f[j - 2], f[j - 1], f[j])
                k = 1

        h = hf

    return summation

# Parameters for the integration
t0 = 0
tn = 10
n_segments = [2, 4, 8, 16, 32]

for segments in n_segments:
    # Define the time values and corresponding velocities
    t_values = [t0 + i * (tn - t0) / segments for i in range(segments + 1)]
    v_values = [v(t) for t in t_values]

    # Perform integration using the Uneven function
    distance = Uneven(segments, t_values, v_values)
    
    # Display the results
    print(f"Segments: {segments}, Distance: {distance} meters")

# Exact value of the integral
exact_value = 289.43515
print(f"\nExact Value: {exact_value} meters")