import cv2 as cv
import numpy as np
import math
from pathlib import Path
import shutil

#for file in $(ls -v *.txt); do clear; cat "$file"; sleep 0.04; done 
#to run it



def clear_directory_pathlib(dir_path):
    path = Path(dir_path)
    for child in path.iterdir():
        if child.is_file() or child.is_symlink():
            child.unlink()
        elif child.is_dir():
            shutil.rmtree(child)

clear_directory_pathlib('./conversion')

file_num = 0

gscale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
chararray = list(gscale)
interval = len(chararray)/256
cap = cv.VideoCapture('video.mp4')

orig_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
orig_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS)

target_width = 269  # Change this to your desired width
#aspect_ratio = orig_height / orig_width
#target_height = int(target_width * aspect_ratio)
target_height = 70

new_dimensions = (target_width, target_height)

def getChar(inputInt):
    return chararray[math.floor(inputInt*interval)]
def rgb_color(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Video playback finished.")
        break

    #lower the resolution
    resized_frame = cv.resize(frame, new_dimensions, interpolation=cv.INTER_AREA)
    with open(f"conversion/{file_num}.txt", "w") as text_file:
        for i in range(target_height):
            line_chars = []
            for j in range(target_width):
                b, g, r = resized_frame[i, j]
                h = int(r/3 + g/3 + b/3)
                c = getChar(h)
                d = rgb_color(r, g, b, c)
                line_chars.append(d)
            text_file.write("".join(line_chars) + "\n")

    file_num = file_num + 1
    
    k = cv.waitKey(5) & 0xFF
    if k == 3 or k == ord('q'):
        break
  

cap.release()
cv.destroyAllWindows()

