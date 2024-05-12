import time
from picamera2 import Picamera2


class CameraClient:
    def __init__(self):
        self.picam2 = None
        self._init_client()

    def _init_client(self):
        self.picam2 = Picamera2()
        preview_config = self.picam2.create_preview_configuration(main={"format": "XRGB8888", "size": (1920, 1080)})
        self.picam2.configure(preview_config)
        self.picam2.start()

    def capture_snapshot(self):
        self.picam2.capture_file(f"snapshot_{int(time.time())}.jpg")