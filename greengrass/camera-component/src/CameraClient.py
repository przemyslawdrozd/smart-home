import time
from picamera2 import Picamera2


class CameraClient:
    def __init__(self):
        self.picam2 = None
        self._init_client()

    def _init_client(self):
        try:
            self.picam2 = Picamera2()
            preview_config = self.picam2.create_preview_configuration(main={"format": "XRGB8888", "size": (1920, 1080)})
            self.picam2.configure(preview_config)
            self.picam2.start()
        except IndexError as e:
            raise RuntimeError(
                "No camera devices found or accessible. Please check the device permissions and connections.") from e
        except PermissionError as e:
            raise RuntimeError(
                "Permission denied while accessing camera devices. Ensure the process has appropriate permissions.") from e

    def capture_snapshot(self):
        self.picam2.capture_file(f"/greengrass/files/camera/snapshot_{int(time.time())}.jpg")
