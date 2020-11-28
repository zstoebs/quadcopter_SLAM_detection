"""FFmpeg based vision demo for Parrot Anafi"""
import threading
import time

import cv2
from pyparrot.Anafi import Anafi
from pyparrot.DroneVision import DroneVision
from pyparrot.Model import Model


# Set to True to output images
WRITE_IMAGES = False

# Speed of the drone
S = 20
S2 = 5
UDOffset = 150

# this is just the bound box sizes that openCV spits out *shrug*
faceSizes = [1026, 684, 456, 304, 202, 136, 90]

# These are the values in which kicks in speed up mode, as of now, this hasn't been finalized or fine tuned so be careful
# Tested are 3, 4, 5
acc = [500,250,250,150,110,70,50]

# Frames per second of the pygame window display
FPS = 25
dimensions = (960, 720)

#
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

class UserVision:
    def __init__(self, vision):
        self.index = 0
        self.vision = vision
        self.cap = None

    def save_pictures(self, args):
        img = self.vision.get_latest_valid_picture()
        if img is not None and WRITE_IMAGES:
            cv2.imwrite(f"image_{self.index:06d}.png", img)
            self.index += 1


if __name__ == "__main__":
    anafi = Anafi()

    if anafi.connect(num_retries=3):
        print("Anafi connected")

        # State information
        print("Updating state information")
        anafi.smart_sleep(1)
        anafi.ask_for_state_update()
        anafi.smart_sleep(1)

        # Vision
        print("Starting vision")
        anafi_vision = DroneVision(anafi, Model.ANAFI)
        user_vision = UserVision(anafi_vision)
        anafi_vision.set_user_callback_function(
            user_vision.save_pictures, user_callback_args=None
        )

        # Video feed
        if anafi_vision.open_video():
            print("Opened video feed")
            
            anafi.safe_takeoff(5)
            anafi.move_relative(dx=0,dy=-0.5,dz=0,dradians=0)
            anafi.safe_land(5)
            
            print("Closing video feed")
            anafi_vision.close_video()
            anafi.smart_sleep(5)
        else:
            print("Could not open video feed")

        print("Anafi disconnected")
        anafi.disconnect()
    else:
        print("Could not connect to Anafi")
