import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt

print(f"OpenCV versão: {cv2.__version__}")
print(f"NumPy versão: {np.__version__}")
print(f"Tesseract: {pytesseract.get_tesseract_version()}")