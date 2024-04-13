import os
BUBBLE_WRAP_EXTRA_INCHES = 2;
PEANUTS_EXTRA_INCHES = 1;

def read_custom_boxes(default_filename='boxess.txt'):
    try:
        # Attempt to read from custom_boxes.txt
        file_path = os.path.join(os.getcwd(), 'custom_boxes.txt')
        with open(file_path, 'r') as file:
            content = file.readlines()
        # Parse the content
        boxes = [tuple(map(int, line.strip().split('x'))) for line in content if line.strip()]
        return boxes
    except FileNotFoundError:
        # If custom_boxes.txt is not found, fall back to the default filename
        with open(default_filename, 'r') as file:
            content = file.readlines()
        # Parse the content
        boxes = [tuple(map(int, line.strip().split('x'))) for line in content if line.strip()]
        return boxes

def find_closest_box(boxes, item_dimensions, bubble_wrap = False, peanuts= False):
    """Finds the closest box to fit the given item dimensions."""
    item_length, item_width, item_height = item_dimensions

    # optional peanuts or bubble wrap dimension modification
    if bubble_wrap:
        item_length+= BUBBLE_WRAP_EXTRA_INCHES
        item_width+= BUBBLE_WRAP_EXTRA_INCHES
        item_height+= BUBBLE_WRAP_EXTRA_INCHES
    if peanuts:
        item_length+=PEANUTS_EXTRA_INCHES
        item_width+= PEANUTS_EXTRA_INCHES
        item_height+= PEANUTS_EXTRA_INCHES
    closest_box = None
    closest_diff = float('inf')

    for box in boxes:
        box_length, box_width, box_height = box
        diff = abs(box_length - item_length) + abs(box_width - item_width) + abs(box_height - item_height)
        if diff < closest_diff:
            closest_diff = diff
            closest_box = box

    return closest_box

def main():
    # Prompt the user to input the item's dimensions
    item_length = int(input("Enter the item's length: "))
    item_width = int(input("Enter the item's width: "))
    item_height = int(input("Enter the item's height: "))

    # Read box dimensions from the file
    boxes = read_custom_boxes()

    # Find the closest box
    closest_box = find_closest_box(boxes, (item_length, item_width, item_height))

    if closest_box:
        print(f"The closest box to fit the item is: {closest_box[0]}x{closest_box[1]}x{closest_box[2]}")
    else:
        print("No boxes found in the file.")

if __name__ == "__main__":
    main()
