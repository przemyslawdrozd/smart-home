import sys
from src.CameraClient import CameraClient
from src.MqttListener import MqttListener
from src.S3Client import S3Client

BUCKET_NAME = "dev-przemo-device-storage"


def main():
    try:
        args = sys.argv[1:]
        print("Create S3 Client")
        s3_client = S3Client(BUCKET_NAME)

        print("Start camera component")
        camera_client = CameraClient(s3_client)

        print("Create MQTT Client")
        mqtt_client = MqttListener(camera_client)

        print("Waiting for messages...")
        mqtt_client.loop_connection()

    except Exception as e:
        print("Error in main:", e)


if __name__ == "__main__":
    main()
