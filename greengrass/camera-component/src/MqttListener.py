import time
import paho.mqtt.client as mqtt

class MqttListener:
    def __init__(self, camera_client):
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
            self.camera_client.capture_snapshot("custom_param")

        except Exception as e:
            print("Error capturing snapshot:", e)

    def loop_connection(self):
        self.client.loop_start()
        while True:
            time.sleep(1)
