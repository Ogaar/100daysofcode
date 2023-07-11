# Import packages
import pyautogui
import cv2
import bezier_curve_movement
import random

# Required images
chop_down_tree_message_path = "C:\\Users\\oscar\\OneDrive\\Documents\\100daysofcode\\100daysofco0de\\woodcutter\\" \
                              "resources\\chop_down_tree.png"
tree_leaves_path = "C:\\Users\\oscar\\OneDrive\\Documents\\100daysofcode\\100daysofcode\\woodcutter\\resources\\" \
                   "tree_leaves.PNG"

# Define function to find and cut down tree

def cut(tree_path, leaves_path):
    found_tree = False

    while found_tree == False:
        tree_leaves_image = pyautogui.locateOnScreen(leaves_path, grayscale=True, confidence=.5)
        if tree_leaves_image:
            bezier_curve_movement.move_mouse_to_point_with_offset(tree_leaves_image)
            print("found tree")
            tree_image = pyautogui.locateOnScreen(tree_path, grayscale=True, confidence=.5)

            if tree_image:
                found_tree = True

        if found_tree:
            print("Cutting...")
            pyautogui.click()

def main():
    cut(chop_down_tree_message_path, tree_leaves_path)

main()


