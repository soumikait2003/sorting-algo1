import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

# Function to generate random data
def generate_data(n):
    return random.sample(range(1, 100), n)

# Bubble Sort algorithm
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            yield data

# Merge Sort algorithm
def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        yield from merge_sort(left_half)
        yield from merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1
            yield data

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1
            yield data

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1
            yield data

# Quick Sort algorithm
def quick_sort(data, low, high):
    if low < high:
        pi = partition(data, low, high)

        yield from quick_sort(data, low, pi-1)
        yield from quick_sort(data, pi+1, high)

def partition(data, low, high):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
        yield data
    data[i+1], data[high] = data[high], data[i+1]
    yield data
    return i+1

# Selection Sort algorithm
def selection_sort(data):
    n = len(data)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if data[j] < data[min_index]:
                min_index = j
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
        yield data

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_title("Sorting Algorithm Visualization")
bar_rects = ax.bar(range(len(generate_data(20))), generate_data(20), align="edge")

# Function to update the plot
def update_plot(frame, rects, algorithm):
    for rect, val in zip(rects, frame):
        rect.set_height(val)
    ax.set_ylabel("Value")
    ax.set_xlabel(f"Iteration {frame_count[0]}")
    frame_count[0] += 1

# Define the number of frames
frame_count = [0]

# Prompt the user to select the sorting algorithm
print("Choose a sorting algorithm:")
print("1. Bubble Sort")
print("2. Merge Sort")
print("3. Quick Sort")
print("4. Selection Sort")
choice = int(input("Enter your choice (1/2/3/4): "))

# Choose the sorting algorithm based on user input
if choice == 1:
    sorting_algorithm = bubble_sort(generate_data(20))
elif choice == 2:
    sorting_algorithm = merge_sort(generate_data(20))
elif choice == 3:
    sorting_algorithm = quick_sort(generate_data(20), 0, len(generate_data(20))-1)
elif choice == 4:
    sorting_algorithm = selection_sort(generate_data(20))
else:
    print("Invalid choice. Exiting...")
    exit()

# Animate the sorting algorithm
anim = animation.FuncAnimation(fig, update_plot, fargs=(bar_rects, sorting_algorithm), frames=range(1, 400), repeat=False)

# Show the plot
plt.show()
