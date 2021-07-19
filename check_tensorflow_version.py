import os
import re
import time
import json
import PIL.Image
import PIL.ImageFont
import PIL.ImageDraw
import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds

from tensorflow.keras.applications.resnet50 import ResNet50
from matplotlib import pyplot as plt

print("Tensorflow version " + tf.__version__)

