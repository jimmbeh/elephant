from picamera2 import Picamera2
from libcamera import Transform
import cv2
import time

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

try:
    while True:
        frame = cam.capture_array()  # Capture frame
        cv2.imshow("Live Preview", frame)  # Show live preview
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Close on 'q' key press
            break
except KeyboardInterrupt:
    print("\nStopping preview...")

# Cleanup
cv2.destroyAllWindows()
cam.stop()
