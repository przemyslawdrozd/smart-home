import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.S3Client import S3Client
from src.MqttListener import MqttListener

BUCKET_NAME = "dev-przemo-device-storage"


def main():
    args = sys.argv[1:]

    print("Create S3 Client")
    s3_client = S3Client(BUCKET_NAME)

    mqtt_client = MqttListener(s3_client)

    s3_client.upload("/greengrass/files/camera/test.jpg")

    print("Waiting for messages...")
    mqtt_client.loop_connection()


if __name__ == "__main__":
    main()
