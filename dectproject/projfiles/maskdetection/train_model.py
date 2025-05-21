import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

dataset_path = "dataset"
with_mask_path = os.path.join(dataset_path, "with_mask")
without_mask_path = os.path.join(dataset_path, "without_mask")

X, y = [], []
for filename in os.listdir(with_mask_path):
    img_path = os.path.join(with_mask_path, filename)
    img = cv2.imread(img_path)

    if img is None:
        print(f"Skipping unreadable image: {filename}")
        continue
    img = cv2.resize(img, (64, 64))
    X.append(img)
    y.append(1) 

for filename in os.listdir(without_mask_path):
    img_path = os.path.join(without_mask_path, filename)
    img = cv2.imread(img_path)

    if img is None:
        print(f" Skipping unreadable image: {filename}")
        continue
    img = cv2.resize(img, (64, 64))
    X.append(img)
    y.append(0)  

X = np.array(X) / 255.0  
y = to_categorical(y, num_classes=2)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential([
    Conv2D(32, (3,3), activation="relu", input_shape=(64,64,3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation="relu"),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation="relu"),
    Dense(2, activation="softmax")
])
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

model.save("mask_detector_model.h5")
print("Model trained and saved successfully!")

