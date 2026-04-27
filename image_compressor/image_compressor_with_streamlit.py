import streamlit as st
import matplotlib.pyplot as plt
import cv2
from tools import Tools as ts

image = cv2.imread("random_image.jpg", cv2.IMREAD_GRAYSCALE)

print(image)
