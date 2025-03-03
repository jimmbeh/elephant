from picamera2 import Picamera2
from libcamera import Transform
import cv2
import time
import os
from datetime import datetime

# Initialize camera with 180-degree rotation
cam = Picamera2()
camera_config = cam.create_preview_configuration({"size": (1080, 720)}, transform=Transform(hflip=1, vflip=1))
cam.configure(camera_config)

# Camera control defaults (adjust as needed)
cam.set_controls({
    "AnalogueGain": 0,  
    "ExposureTime": 10000,  
    "Contrast": 1.0,  
    "Brightness": 0,  
    "Saturation": 1.0,  
    "Sharpness": 1.0   
})

# Start camera
cam.start()
time.sleep(2)  # Camera warm-up

# Create output directory if it doesn't exist
output_dir = "/home/argon/desktop/Videos"
os.makedirs(output_dir, exist_ok=True)

# Generate filename with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
video_filename = f"{output_dir}/video_{timestamp}.mp4"

# Video recording setup
fps = 20  # Frames per second
frame_size = (1080, 720)  # Match camera resolution
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec for .mp4 format
out = cv2.VideoWriter(video_filename, fourcc, fps, frame_size)

print(f"Recording video: {video_filename}")
RECORD_SECONDS = 10  # Set duration or use Ctrl+C to stop

start_time = time.time()
try:
    while time.time() - start_time < RECORD_SECONDS:
        frame = cam.capture_array()  # Capture frame
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert color for OpenCV
        out.write(frame)  # Save frame to video file
except KeyboardInterrupt:
    print("\nRecording stopped manually.")

# Cleanup
out.release()
cam.stop()
print(f"Video saved at: {video_filename}")
