import sys
from src.CameraClient import CameraClient
from src.MqttListener import MqttListener


def main():
    try:
        args = sys.argv[1:]
        print("Start camera component")

        camera_client = CameraClient()
        mqtt_client = MqttListener(camera_client)

        print("Waiting for messages...")
        mqtt_client.loop_connection()

    except Exception as e:
        print("Error in main:", e)


if __name__ == "__main__":
    main()
