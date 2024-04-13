from flask import Flask, request, render_template, jsonify
import boxfinder



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item_length = int(request.form.get('item_length'))
        item_width = int(request.form.get('item_width'))
        item_height = int(request.form.get('item_height'))
        bubble_wrap = 'bubble_wrap' in request.form 
        peanuts = 'peanuts' in request.form
        boxes = boxfinder.read_custom_boxes('boxes.txt')
        closest_box = boxfinder.find_closest_box(boxes, (item_length, item_width, item_height), bubble_wrap, peanuts)
        return render_template('result.html', closest_box=closest_box)
    return render_template('index.html')


@app.route('/save-boxes', methods=['POST'])
def save_boxes():
    print("POST request received for /save-boxes")
    # Correctly access JSON data
    data = request.get_json()
    custom_boxes = data.get('customBoxes') if data else None
    print(custom_boxes)
    try:
        with open('custom_boxes.txt', 'w') as file:
            file.write(custom_boxes)
        return jsonify({'message': 'Boxes saved!!'}), 200
    except Exception as e:
        print(f"Error saving custom boxes: {e}")
        return jsonify({'error': 'Error saving boxes'}), 500

if __name__ == "__main__":
    app.run(debug=True)