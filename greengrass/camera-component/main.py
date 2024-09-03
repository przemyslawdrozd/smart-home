import sys
from src.CameraClient import CameraClient
import json
import time
import paho.mqtt.client as mqtt

# MQTT Broker details
broker = "localhost"  # Use "localhost" if using a local broker
port = 1883
topic = "camera/snapshot"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(topic)
        print(f"Subscribed to topic: {topic}")
    else:
        print("Failed to connect, return code %d\n", rc)


def on_message(client, userdata, msg):
    print(f"Message received: {msg.payload.decode()} on topic {msg.topic}")
    try:
        # Assuming that any message received on this topic triggers a snapshot
        camera_client.capture_snapshot()
        print("Snapshot created")
    except Exception as e:
        print("Error capturing snapshot:", e)


def main():
    try:
        print("Start camera component")
        args = sys.argv[1:]

        global camera_client
        camera_client = CameraClient()
        print("Camera client connected")

        # MQTT Client setup
        mqtt_client = mqtt.Client()
        mqtt_client.on_connect = on_connect
        mqtt_client.on_message = on_message

        # Connect to the MQTT broker
        mqtt_client.connect(broker, port)

        # Start the MQTT client loop
        mqtt_client.loop_start()

        print("Waiting for messages...")

        # Keep the main thread alive to listen for messages indefinitely
        while True:
            time.sleep(1)

    except Exception as e:
        print("Error in main:", e)


if __name__ == "__main__":
    main()
