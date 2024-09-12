import sys
from src.CameraClient import CameraClient
from src.MqttListener import MqttListener




def main():
    try:
        args = sys.argv[1:]
        # print("Create S3 Client")
        # s3_client = S3Client(BUCKET_NAME)

        print("Start camera component")
        camera_client = CameraClient()

        print("Create MQTT Client")
        mqtt_client = MqttListener(camera_client)

        print("Waiting for messages...")
        mqtt_client.loop_connection()

    except Exception as e:
        print("Error in main:", e)


if __name__ == "__main__":
    main()
