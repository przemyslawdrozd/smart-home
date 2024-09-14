import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.CameraClient import CameraClient
from src.MqttListener import MqttListener
from src.MqttPublisher import MqttPublisher


def main():
    try:
        args = sys.argv[1:]
        # print("Create S3 Client")
        # s3_client = S3Client(BUCKET_NAME)
        print("Create MQTT Publisher")
        mqtt_publisher = MqttPublisher()

        print("Start camera component")
        camera_client = CameraClient()

        print("Create MQTT Listener")
        mqtt_client = MqttListener(mqtt_publisher, camera_client)

        print("Waiting for messages...")
        mqtt_client.loop_connection()

    except Exception as e:
        print("Error in main:", e)


if __name__ == "__main__":
    main()
