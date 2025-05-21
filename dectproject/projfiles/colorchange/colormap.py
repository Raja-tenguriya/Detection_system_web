import cv2
import sys
import os

print(f"Arguments received: {sys.argv}")

if len(sys.argv) < 2:
    print("Error: No image file provided.")
    sys.exit(1)

image_path = sys.argv[1] 

if not os.path.exists(image_path):
    print(f"Error: File does not exist at {image_path}")
    sys.exit(1)

image = cv2.imread(image_path)
if image is None:
    print("Error: Could not read the image file.")
    sys.exit(1)

colormap_image = cv2.applyColorMap(image, cv2.COLORMAP_JET)

print(f"Color Mapped Image Shape: {colormap_image.shape}")

output_dir = os.path.join(os.path.dirname(image_path), "colormapout")
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "output_colormap.jpg")
cv2.imwrite(output_path, colormap_image)

if os.path.exists(output_path):
    print(f"Color-mapped image successfully saved at: {output_path}")
else:
    print("Error: Image not saved.")

sys.exit(0)
