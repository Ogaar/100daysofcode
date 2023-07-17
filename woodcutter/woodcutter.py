# Import packages
import time
from datetime import datetime

import mouse as mouse
import pyautogui
import cv2
from PIL import ImageGrab

import bezier_curve_movement
import random
import numpy as np

# Required images
chop_down_tree_message_path = "C:\\Users\\oscar\\OneDrive\\Desktop\\test\\choptreemessage.png"
chop_down_oak_message_path = "C:\\Users\\oscar\\OneDrive\\Documents\\100daysofcode\\100daysofcode\\woodcutter\\" \
                             "resources\\chopoakmessage.png"

# Define the screen capture dimensions
screen_width, screen_height = 1920, 1080  # Modify these values according to your screen resolution

# Define function to find and cut down tree

def cut(tree_path):
    found_tree = False
    # Capture the screen image
    location_x = []
    location_y = []
    while found_tree == False:
        num_of_logs = count_logs()
        if num_of_logs >= 26:
            drop_logs()
        if pyautogui.locateOnScreen(tree_path, grayscale=True, confidence=.9):
            print("Cutting...")
            pyautogui.click()
            num_of_logs = count_logs()
            current_time = time.time()
            while num_of_logs == count_logs():
                if time.time() - current_time > 15:
                    break
                pass
        else:
            screen = np.array(ImageGrab.grab(bbox=(0, 0, screen_width, screen_height)))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            # Apply shape detection algorithms (example: circle detection using Hough Transform)
            circles = cv2.HoughCircles(
                screen,
                cv2.HOUGH_GRADIENT,
                dp=1,
                minDist=150,
                param1=50,
                param2=25,
                minRadius=45,
                maxRadius=100)
            circles = np.uint16(np.around(circles))
            circles = organise_array(circles[0])
            if circles is not None:
                # Iterate over detected circles

                for circle in circles:
                    mouse.move(circle[0], circle[1])
                    location_x.append(circle[0])
                    location_y.append(circle[1])
                    if pyautogui.locateOnScreen(tree_path, grayscale=True, confidence=.9):
                        print("Breaking...")
                        break
                mouse.move(location_x[-2],location_y[-2])
                pyautogui.sleep(.5)
                print("Cutting...")
                pyautogui.click()
                num_of_logs = count_logs()
                current_time = time.time()
                while num_of_logs == count_logs():
                    if time.time() - current_time > 15:
                        break
                    pass



def organise_array(circles):
    distances = np.sqrt((circles[:, 0] - 960)**2 + (circles[:, 1] - 540)**2)
    sorted_indices = np.argsort(distances)
    sorted_circles = circles[sorted_indices]
    return sorted_circles

def count_logs():
    image_path = "C:\\Users\\oscar\\OneDrive\\Documents\\100daysofcode\\100daysofcode\\woodcutter\\" \
                            "resources\\inventory_logs.PNG"
    inventory = np.array(ImageGrab.grab(bbox=(1689, 738, 1873, 994)))
    inventory_gray = cv2.cvtColor(inventory, cv2.COLOR_RGB2GRAY)
    image = cv2.imread(image_path, 0)
    result = cv2.matchTemplate(inventory_gray, image, cv2.TM_CCOEFF_NORMED)

    # Set a threshold for matches
    threshold = 0.8
    matches = np.where(result >= threshold)

    # Count the number of matches
    count = len(matches[0])

    return count

def drop_logs():
    image_path = "C:\\Users\\oscar\\OneDrive\\Documents\\100daysofcode\\100daysofcode\\woodcutter\\" \
                 "resources\\inventory_logs.PNG"
    inventory = np.array(ImageGrab.grab(bbox=(1689, 738, 1873, 994)))
    inventory_gray = cv2.cvtColor(inventory, cv2.COLOR_RGB2GRAY)
    image = cv2.imread(image_path, 0)
    result = cv2.matchTemplate(inventory_gray, image, cv2.TM_CCOEFF_NORMED)

    # Set a threshold for matches
    threshold = 0.8
    matches = np.where(result >= threshold)

    # Drop the logs
    pyautogui.keyDown('shift')
    y_list = list(matches[0])
    x_list = list(matches[1])
    for i in range(0, len(x_list)):
        mouse.move(x_list[i] + 1700, y_list[i] + 745)
        pyautogui.sleep(.8)
        pyautogui.click()
    pyautogui.keyUp('shift')

    return matches



def main():
    tree_choice = input("What type of tree would you like to cut? (Normal/Oak)\n").lower()
    if tree_choice == "oak":
        tree_path = chop_down_oak_message_path
    elif tree_choice == "normal":
        tree_path = chop_down_tree_message_path
    cut(tree_path)


main()


