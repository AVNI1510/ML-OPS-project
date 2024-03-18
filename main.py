from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def selection_sort(numbers):
    steps = [list(numbers)]  # Initial step with the original list
    for i in range(len(numbers)):
        min_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        steps.append(list(numbers))  # Append a copy of numbers
    return steps

@app.route('/')
def index():
    return render_template('index_selection.html')

@app.route('/sort_selection', methods=['POST'])
def sort_numbers_selection():
    numbers = request.form.get('numbers')
    numbers = [int(num) for num in numbers.split(',') if num.strip()]
    steps = selection_sort(numbers)
    return jsonify(steps)

if __name__ == '__main__':
    app.run(debug=True)
