import pyautogui
import math
import random


def compute_bezier_point(p0, p1, p2, p3, t):
    """Compute a point on a cubic Bezier curve given control points and parameter t."""
    x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]
    y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
    return x, y


def move_mouse_to_point_with_offset(point, offset_range=(1, 3), num_points=100, duration=1):
    """Move the mouse cursor to the given point with a random offset, following a Bezier curve."""
    control_points = [
        pyautogui.position(),  # Current mouse position as the first control point
        ((point[0] + pyautogui.position()[0]) // 2, (point[1] + pyautogui.position()[1]) // 2),  # Second control point
        ((point[0] + pyautogui.position()[0]) // 2, (point[1] + pyautogui.position()[1]) // 2),  # Third control point
        point  # Destination point
    ]

    points = []
    for i in range(num_points):
        t = i / (num_points - 1)
        offset = random.randint(offset_range[0], offset_range[1])
        offset_point = (point[0] + random.randint(-offset, offset),
                        point[1] + random.randint(-offset, offset))
        points.append(offset_point)

    total_duration = duration
    interval = total_duration / num_points

    for point in points:
        pyautogui.moveTo(point[0], point[1], duration=interval)