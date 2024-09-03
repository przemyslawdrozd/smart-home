import threading
import traceback
import awsiot.greengrasscoreipc.clientv2 as clientV2
import json
import paho.mqtt.client as mqtt

SHADOW_TOPIC = '$aws/things/RPI4Desk/shadow/update/accepted'
QOS = '1'

# MQTT Broker details (local)
broker = "localhost"
port = 1883
topic = "camera/snapshot"


class ShadowManager:
    def __init__(self):
        self.ipc_client = clientV2.GreengrassCoreIPCClientV2()
        self.operation = None
        print("Connected to IPC V2")

        self.client = mqtt.Client()
        self.client.on_publish = self.on_mqtt_publish
        self.client.connect(broker, port)

    def on_mqtt_publish(self, client, userdata, result):
        print(f"Data published to {topic}")

    def subscribe_to_topic(self):
        resp, operation = self.ipc_client.subscribe_to_iot_core(
            topic_name=SHADOW_TOPIC,
            qos=QOS,
            on_stream_event=self.on_stream_event,
            on_stream_error=self.on_stream_error,
            on_stream_closed=self.on_stream_closed
        )
        self.operation = operation
        print("Resp on subscribe", resp)

    def on_stream_event(self, event):
        try:
            topic_name = event.message.topic_name
            message = str(event.message.payload, 'utf-8')
            print(f'Received new message on topic {topic_name}:  {message}')
            self.client.publish(topic, message)
        except:
            traceback.print_exc()

    # Return True to close stream, False to keep stream open.
    def on_stream_error(self, error):
        print("Error on stream", error)
        return True

    def on_stream_closed(self):
        print("Stream in closed")
        pass

    def keep_loop_connection(self):
        event = threading.Event()
        event.wait()

    def close_connection(self):
        # To stop subscribing, close the operation stream.
        self.operation.close()
        self.ipc_client.close()
