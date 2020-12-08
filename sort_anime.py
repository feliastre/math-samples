import random
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation

def bubble_sort_frames(a):
    frames = []
    frames.append(a)
    not_sorted = True
    x = a[:]
    while not_sorted:
        not_sorted = False
        for i in range(len(x) - 1):
            if x[i] > x[i + 1]:
                x = x[:]
                x[i], x[i + 1] = x[i + 1], x[i]
                frames.append(x)
                not_sorted = True
    return frames

def q_sort_frames(a, l, r, frames = []):
    i, j = l, r
    while i < j:
        while i < j and a[i] <= a[j]:
            i = i + 1

        if i < j:
            a[i], a[j] = a[j], a[i]
            frames.append(a[:])

        while i < j and a[i] <= a[j]:
            j = j - 1

        if i < j:
            a[i], a[j] = a[j], a[i]
            frames.append(a[:])

    if i - 1 > l:
        q_sort_frames(a, l, i - 1, frames)

    if i + 1 < r:
        q_sort_frames(a, i + 1, r, frames)
    

def q_sort_frames_total(a, frames = []):
    frames.append(a)
    q_sort_frames(a, 0, len(a) - 1, frames)
    return frames


def prepare_unsorted_arrays():
    length = 20
    count = 4
    data_qsort = []
    data_bubble = []

    random.seed()
    ordered_init = [i + 1 for i in range(length)]

    for _ in range(count):
        y = ordered_init[:]
        random.shuffle(y)
        frames = []
        y_ = y[:]
        data_qsort.append(q_sort_frames_total(y, frames))
        data_bubble.append(bubble_sort_frames(y_))

    return data_qsort + data_bubble

def get_frames_for_animation(data):
    n_frames = max(len(a) for a in data)
    frames = [[data[i][min(j, len(data[i]) - 1)] for i in range(len(data))] for j in range(n_frames)]
    return frames

data = prepare_unsorted_arrays()

frames = get_frames_for_animation(data)

fig = plt.figure()
plot =plt.imshow(frames[0])

def init():
    plot.set_data(frames[0])
    return [plot]

def animate(index):
    plot.set_data(frames[index])
    return [plot]

anim = FuncAnimation(fig, animate, init_func = init, frames=len(frames), interval = 200, blit=True)

anim.save("qsort.gif")
plt.show()
