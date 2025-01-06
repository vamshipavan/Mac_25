def find_overlap(box1, box2):
    """
    Finds the overlap region of two bounding boxes.

    Parameters:
    - box1: A tuple (x1, y1, x2, y2) where (x1, y1) is the top-left and (x2, y2) is the bottom-right corner.
    - box2: A tuple (x1, y1, x2, y2) where (x1, y1) is the top-left and (x2, y2) is the bottom-right corner.

    Returns:
    - A tuple (x1, y1, x2, y2) representing the overlap region, or None if there is no overlap.
    """
    # Calculate the intersection coordinates
    x1 = max(box1[0], box2[0])  # Max of the left edges
    y1 = max(box1[1], box2[1])  # Max of the top edges
    x2 = min(box1[2], box2[2])  # Min of the right edges
    y2 = min(box1[3], box2[3])  # Min of the bottom edges

    # Check if there is an overlap
    if x1 < x2 and y1 < y2:
        return (x1, y1, x2, y2)  # Return the overlap region
    else:
        return None  # No overlap

def main():
    # Define two bounding boxes
    box1 = (2, 3, 8, 9)  # Format: (x1, y1, x2, y2)
    box2 = (5, 6, 10, 12)

    # Find and print the overlap
    overlap = find_overlap(box1, box2)

    if overlap:
        print(f"Overlap region: {overlap}")
    else:
        print("No overlap.")

if __name__ == "__main__":
    main()

