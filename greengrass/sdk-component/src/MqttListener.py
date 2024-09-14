import time
import traceback
import paho.mqtt.client as mqtt
from S3Client import S3Client


class MqttListener:
    def __init__(self, s3_client: S3Client):
        self.s3_client = s3_client
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        # Connect to the MQTT broker
        self.client.connect(host="127.0.0.1", port=1883, keepalive=60)

    @staticmethod
    def on_connect(client, userdata, flags, rc, properties=None):
        if rc == 0:
            print("Connected to MQTT Broker!")
            client.subscribe("camera/upload")
            print(f"Subscribed to topic: camera/upload")
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_message(self, client, userdata, msg):
        print(f"Message received: {msg.payload.decode()} on topic {msg.topic}")
        try:
            # Assuming that any message received on this topic triggers a snapshot
            file_name = msg.payload.decode()
            self.s3_client.upload(file_name)
        except Exception as e:
            print("Error on_message MqttListener", e)
            traceback.print_exc()

    def loop_connection(self):
        self.client.loop_start()
        while True:
            time.sleep(1)
