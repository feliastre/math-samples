import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import cos, sin, pi, sqrt

def vector_from_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return x2 - x1, y2 - y1

def point_as_shift(p, v):
    x, y = p
    dx, dy = v
    return x + dx, y + dy

def vector_mul_scalar(v, a):
    x, y = v
    return x * a, y * a

def vector_rotated(v, alpha):
    x, y = v
    return x * cos(alpha) - y * sin(alpha), x * sin(alpha) + y * cos(alpha)

def sum_vectors(v1, v2):
    x1, y1 = v1
    x2, y2 = v2

    return x1 + x2, y1 + y2

def transform(p1, p2, is_left = True):
    v = vector_from_points(p1, p2)
    v1 = vector_rotated(v, (-1. if is_left else 1.) * pi / 4.)
    v1 = vector_mul_scalar(v1, 1. / sqrt(2.))
    return [p1, point_as_shift(p1, v1)]

points = [(0, 0), (1, 1)]
frames = [points]

for _ in range(15):
    is_left = True
    new_points = []
    for i in range(len(points) - 1):
        new_points.extend(transform(points[i], points[i + 1], i % 2 == 0))
    new_points.append(points[-1])
    points = new_points
    frames_x = [p[0] for p in new_points]
    frames_y = [p[1] for p in new_points]
    frames.append((frames_x, frames_y))

def init():
    return plt.plot(frames[0][0], frames[0][1])
def animate(index):
    return plt.plot(frames[index][0], frames[index][1])

fig = plt.figure()
anim = FuncAnimation(fig, animate, init_func = init, frames=len(frames), interval = 1000, blit=True)

anim.save("dragon.gif")
plt.show()
