import sys
from src.CameraClient import CameraClient


def main():
    try:
        print("Start camera component")
        args = sys.argv[1:]

        camera_client = CameraClient()
        print("Camera client connected")

        camera_client.capture_snapshot()
        print("Snapshot created")

    except Exception as e:
        print("Error on main", e)


if __name__ == "__main__":
    main()
