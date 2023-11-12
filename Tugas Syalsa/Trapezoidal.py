import math

# Constants
g = 9.8
m = 68.1
c = 12.5

# Function to calculate velocity v(t)
def v(t):
    return g * m / c * (1 - math.exp(-c / m * t))

# Analytical solution for the integral
def analytical_solution():
    return 289.43515

# Trapezoidal single segment
def Trap(h, f0, f1):
    return h * (f0 + f1) / 2

# Trapezoidal multiple segment
def trapm(h, n, f):
    total = f[0] + f[n - 1]  # Add the first and last points
    for i in range(1, n - 1):
        total += 2 * f[i]  # Multiply intermediate points by 2

    return h * total / 2

# Time interval
t0 = 0
t1 = 10

# Number of segments
segments = [1, 2, 5, 10, 20, 50, 100]

# Calculate distance using Trapezoidal rule for different segments
for segment in segments:
    h = (t1 - t0) / segment
    time_points = [t0 + i * h for i in range(segment + 1)]
    velocities = [v(t) for t in time_points]

    # Trapezoidal single segment
    distance_single_segment = Trap(h, velocities[0], velocities[-1])

    # Trapezoidal multiple segment
    distance_multiple_segment = trapm(h, segment + 1, velocities)

    print(f"Segments: {segment}, Single Segment Distance: {distance_single_segment:.5f},"
          f" Multiple Segment Distance: {distance_multiple_segment:.5f}")

# Analytical solution
exact_distance = analytical_solution()
print(f"\nAnalytical Solution: {exact_distance}")