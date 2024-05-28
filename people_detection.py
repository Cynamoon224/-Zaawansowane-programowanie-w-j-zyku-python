"""
Moduł zawierający funkcje do wykrywania ludzi na obrazach.
"""

import os
import cv2
import numpy as np
from imutils.object_detection import non_max_suppression


def detect_people(image, img_format, task_id=None):
    """
    Wykrywa ludzi na obrazie i zapisuje wynikowy obraz z narysowanymi prostokątami wokół wykrytych osób.

    Args:
        image (numpy.ndarray): Obraz wejściowy w formacie numpy array.
        img_format (str): Format zapisu wynikowego obrazu (np. 'jpg', 'png').
        task_id (str, opcjonalne): Identyfikator zadania. Jeśli podany, wynikowy obraz zostanie zapisany z jego użyciem.

    Returns:
        int: Liczba wykrytych osób na obrazie.
    """
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    image = cv2.resize(image, (480, 360))
    boxes, _ = hog.detectMultiScale(image, winStride=(4, 4), scale=1.22, padding=(16, 16))
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    pick = non_max_suppression(boxes, probs=None, overlapThresh=0.65)

    for (x1, y1, x2, y2) in pick:
        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

    people_count = len(pick)
    if task_id:
        path_out = f'obrazy/tasks_output/{task_id}-{people_count}.{img_format}'
    else:
        file_count = len(os.listdir('obrazy/output')) + 1
        path_out = f'obrazy/output/file{file_count}-{people_count}people.{img_format}'

    cv2.imwrite(path_out, image)
    return people_count
