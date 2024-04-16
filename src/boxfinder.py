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
    

# Adjusted dimensions after adding bubble wrap and peanuts
    adjusted_dimensions = (item_length, item_width, item_height)

    # Filter out boxes that are smaller in any dimension compared to the adjusted dimensions
    suitable_boxes = [box for box in boxes if all(item_dim <= box_dim for item_dim, box_dim in zip(adjusted_dimensions, box))]

    if not suitable_boxes:
        return None # No suitable boxes found

    # Find the box with the smallest volume difference that is still large enough to contain the item
    closest_box = min(suitable_boxes, key=lambda box: abs(box[0] * box[1] * box[2] - item_length * item_width * item_height))

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
