import sys
from src.CameraClient import CameraClient


def main():
    args = sys.argv[1:]

    camera_client = CameraClient()

    camera_client.capture_snapshot()


if __name__ == "__main__":
    main()
