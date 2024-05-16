import sys
from src.CameraClient import CameraClient


def main():
    print("Start camera component")
    args = sys.argv[1:]

    camera_client = CameraClient()
    print("Camera client connected")

    camera_client.capture_snapshot()
    print("Snapshot created")

if __name__ == "__main__":
    main()
