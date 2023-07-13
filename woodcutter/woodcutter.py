# Import packages
import mouse as mouse
import pyautogui
import cv2
from PIL import ImageGrab

import bezier_curve_movement
import random
import numpy as np

# Required images
chop_down_tree_message_path = "C:\\Users\\oscar\\OneDrive\\Desktop\\test\\choptreemessage.png"

# Define the screen capture dimensions
screen_width, screen_height = 1920, 1080  # Modify these values according to your screen resolution

# Define function to find and cut down tree

def cut(tree_path):
    found_tree = False
    # Capture the screen image


    while found_tree == False:
        screen = np.array(ImageGrab.grab(bbox=(0, 0, screen_width, screen_height)))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        # Apply shape detection algorithms (example: circle detection using Hough Transform)
        circles = cv2.HoughCircles(
            screen,
            cv2.HOUGH_GRADIENT,
            dp=1,
            minDist=50,
            param1=50,
            param2=30,
            minRadius=50,
            maxRadius=100)
        print(found_tree)
        print(circles)
        if circles is not None:
            # Iterate over detected circles
            for circle in circles[0, :]:
                # bezier_curve_movement.move_mouse_to_point_with_offset(circle)
                mouse.move(circle[0], circle[1])
                tree_image = pyautogui.locateOnScreen(tree_path, grayscale=True, confidence=.45)
                pyautogui.sleep(3)
                if tree_image:
                    print("found tree")
                    found_tree = True
                if found_tree:
                    print("Cutting...")
                    pyautogui.click()
                    continue
            continue

def main():
    not_cutting = True
    while True:
        cut(chop_down_tree_message_path)

main()


