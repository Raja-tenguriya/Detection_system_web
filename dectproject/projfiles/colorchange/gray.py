import cv2
import sys
import os

if len(sys.argv) < 2:
    print("Error: No image file provided.")
    sys.exit(1)

image_path = sys.argv[1]  

image = cv2.imread(image_path)
if image is None:
    print("Error: Could not read the image file.")
    sys.exit(1)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

output_dir = os.path.join(os.path.dirname(image_path), "grayout")
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "output_grayscale.jpg")
cv2.imwrite(output_path, gray_image)

print(f"Grayscale image saved at: {output_path}")
