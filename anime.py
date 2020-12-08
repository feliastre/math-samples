import matplotlib.pyplot as plt
from math import cos, sin, pi
from  matplotlib.animation import FuncAnimation

#0, 0
#№1, 1
#0, 0
#\cos(pi / 3) - sin(pi / 3), sin(pi / 3) + cos(pi / 3)

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


def transform(p1, p2):
    v = vector_from_points(p1, p2)
    x = vector_mul_scalar(v, 1. / 3.)
    x2 = vector_mul_scalar(x, 2.)
    x3 = sum_vectors(x, vector_rotated(x, pi / 3.))

    return [p1, point_as_shift(p1, x), point_as_shift(p1, x3), point_as_shift(p1, x2)]

points = [(0, 0), (1, 1)]

frames = []
for _ in range(10):
    draft = []
    for i in range(len(points) - 1):
        draft.extend(transform(points[i], points[i + 1]))
    draft.append(points[-1])
    points = draft
    frames_x = [p[0] for p in draft]
    frames_y = [p[1] for p in draft]
    frames.append((frames_x, frames_y))

fig = plt.figure()
#plot = plt.plot(frames[0][0], frames[0][1])

def init():
    return plt.plot(frames[0][0], frames[0][1])
def animate(index):
    return plt.plot(frames[index][0], frames[index][1])

anim = FuncAnimation(fig, animate, init_func = init, frames=len(frames), interval = 1000, blit=True)

anim.save("fract.gif")
plt.show()





