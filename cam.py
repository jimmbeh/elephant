from picamera2 import Picamera2
import time

# Initialize camera
cam = Picamera2()

# Configure resolution and video mode
camera_config = cam.create_video_configuration(main={"size": (1280, 720), "format": "YUV420"})
cam.configure(camera_config)

# Set important camera parameters (adjust as needed)
cam.set_controls({
    "Gain": 2.0,           # Adjust between 1.0 - 8.0 for brightness
    "Contrast": 1.5,       # Adjust between 1.0 - 5.0 for better visibility
    "ExposureTime": 500000,  # In microseconds (500ms); reduce if too bright or blurry
    "Brightness": 0.5,     # Adjust if image is too dark or washed out
    "Saturation": 1.0,     # 1.0 for normal colors; reduce for greyscale effect
    "FrameRate": 10.0,     # Lower FPS for better low-light performance
})

# Start camera preview
cam.start()

print("Camera is running. Press Ctrl+C to exit.")
try:
    while True:
        time.sleep(1)  # Keep running, adjust settings if needed
except KeyboardInterrupt:
    print("Stopping camera.")
    cam.stop()
