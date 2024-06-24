# from flask import Flask, render_template, request, redirect, url_for
# import numpy as np
# import matplotlib.pyplot as plt
# import io
# import base64
# import time

# app = Flask(__name__)

# def bubble_sort_visualizer(arr):
#     images = []
#     n = len(arr)
#     fig, ax = plt.subplots()

#     def update_bars(arr, bars):
#         for bar, val in zip(bars, arr):
#             bar.set_height(val)
#         fig.canvas.draw()
#         buf = io.BytesIO()
#         plt.savefig(buf, format='png')
#         buf.seek(0)
#         image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
#         images.append(image_base64)
#         time.sleep(0.1)

#     bars = ax.bar(range(len(arr)), arr, align='edge')
#     plt.ion()
#     plt.show()

#     for i in range(n-1):
#         swapped = False
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#                 update_bars(arr, bars)
#         if not swapped:
#             break

#     plt.ioff()
#     plt.close()
#     return images

# def selection_sort_visualizer(arr):
#     images = []
#     n = len(arr)
#     fig, ax = plt.subplots()

#     def update_bars(arr, bars):
#         for bar, val in zip(bars, arr):
#             bar.set_height(val)
#         fig.canvas.draw()
#         buf = io.BytesIO()
#         plt.savefig(buf, format='png')
#         buf.seek(0)
#         image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
#         images.append(image_base64)
#         time.sleep(0.1)

#     bars = ax.bar(range(len(arr)), arr, align='edge')
#     plt.ion()
#     plt.show()

#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#         update_bars(arr, bars)

#     plt.ioff()
#     plt.close()
#     return images

# def insertion_sort_visualizer(arr):
#     images = []
#     n = len(arr)
#     fig, ax = plt.subplots()

#     def update_bars(arr, bars):
#         for bar, val in zip(bars, arr):
#             bar.set_height(val)
#         fig.canvas.draw()
#         buf = io.BytesIO()
#         plt.savefig(buf, format='png')
#         buf.seek(0)
#         image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
#         images.append(image_base64)
#         time.sleep(0.1)

#     bars = ax.bar(range(len(arr)), arr, align='edge')
#     plt.ion()
#     plt.show()

#     for i in range(1, n):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#         update_bars(arr, bars)

#     plt.ioff()
#     plt.close()
#     return images

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         numbers = request.form['numbers']
#         algorithm = request.form['algorithm']
#         arr = list(map(int, numbers.split(',')))

#         if algorithm == 'bubble':
#             images = bubble_sort_visualizer(arr)
#         elif algorithm == 'selection':
#             images = selection_sort_visualizer(arr)
#         elif algorithm == 'insertion':
#             images = insertion_sort_visualizer(arr)
#         else:
#             return redirect(url_for('index'))

#         return render_template('visualize.html', images=images)

#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)








# from flask import Flask, render_template, request, jsonify
# import time

# app = Flask(__name__)

# def bubble_sort(arr):
#     n = len(arr)
#     steps = []

#     for i in range(n-1):
#         swapped = False
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#             steps.append(arr.copy())
#         if not swapped:
#             break

#     return steps

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/sort', methods=['POST'])
# def sort():
#     data = request.json
#     numbers = list(map(int, data['numbers']))
#     algorithm = data['algorithm']

#     if algorithm == 'bubble':
#         steps = bubble_sort(numbers)
#     else:
#         return jsonify({"error": "Unsupported algorithm"}), 400

#     return jsonify(steps)

# if __name__ == '__main__':
#     app.run(debug=True)









from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def bubble_sort(arr):
    n = len(arr)
    steps = []

    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            steps.append(arr.copy())
        if not swapped:
            break

    return steps

def selection_sort(arr):
    n = len(arr)
    steps = []

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append(arr.copy())

    return steps

def insertion_sort(arr):
    n = len(arr)
    steps = []

    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        steps.append(arr.copy())

    return steps

def merge_sort(arr):
    steps = []

    def merge(left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left if left else right)
        return result

    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])
        sorted_arr = merge(left, right)
        steps.append(sorted_arr)
        return sorted_arr

    merge_sort_recursive(arr)
    return steps

def quick_sort(arr):
    steps = []

    def quick_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        sorted_arr = quick_sort_recursive(left) + middle + quick_sort_recursive(right)
        steps.append(sorted_arr)
        return sorted_arr

    quick_sort_recursive(arr)
    return steps

def radix_sort(arr):
    steps = []
    max1 = max(arr)

    exp = 1
    while max1 / exp >= 1:
        arr = counting_sort(arr, exp)
        steps.append(arr.copy())
        exp *= 10
    return steps

def counting_sort(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp1
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

    return arr

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort():
    data = request.json
    numbers = list(map(int, data['numbers']))
    algorithm = data['algorithm']

    if algorithm == 'bubble':
        steps = bubble_sort(numbers)
    elif algorithm == 'selection':
        steps = selection_sort(numbers)
    elif algorithm == 'insertion':
        steps = insertion_sort(numbers)
    elif algorithm == 'merge':
        steps = merge_sort(numbers)
    elif algorithm == 'quick':
        steps = quick_sort(numbers)
    elif algorithm == 'radix':
        steps = radix_sort(numbers)
    else:
        return jsonify({"error": "Unsupported algorithm"}), 400

    return jsonify(steps)

if __name__ == '__main__':
    app.run(debug=True)
