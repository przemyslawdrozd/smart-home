import time
import traceback
import paho.mqtt.client as mqtt
from MqttPublisher import MqttPublisher
from CameraClient import CameraClient


class MqttListener:
    def __init__(self, mqtt_publisher: MqttPublisher, camera_client: CameraClient):
        self.mqtt_publisher = mqtt_publisher
        self.camera_client = camera_client
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        # Connect to the MQTT broker
        self.client.connect(host="127.0.0.1", port=1883, keepalive=60)

    @staticmethod
    def on_connect(client, userdata, flags, rc, properties=None):
        if rc == 0:
            print("Connected to MQTT Broker!")
            client.subscribe("camera/snapshot")
            print(f"Subscribed to topic: camera/snapshot")
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_message(self, client, userdata, msg):
        print(f"Message received: {msg.payload.decode()} on topic {msg.topic}")
        try:
            # Assuming that any message received on this topic triggers a snapshot
            file_path = self.camera_client.capture_snapshot()
            res = self.mqtt_publisher.client.publish("camera/upload", file_path)
            print("published on camera/upload", res)
        except Exception as e:
            print("Error on_message MqttListener")
            traceback.print_exc()

    def loop_connection(self):
        self.client.loop_start()
        while True:
            time.sleep(1)
