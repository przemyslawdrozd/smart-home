import paho.mqtt.client as mqtt


class MqttPublisher:
    def __init__(self):
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.connect(host="127.0.0.1", port=1883, keepalive=60)
        self.client.on_publish = self.on_mqtt_publish
        self.client.on_disconnect = self.on_disconnect

    @staticmethod
    def on_mqtt_publish(client, userdata, mid, reason_code, properties):
        print(f"Data published to camera/snapshot", mid, reason_code)

    @staticmethod
    def on_disconnect(client, userdata, disconnect_flags, reason_code, properties):
        print("reason_code", reason_code)
        print("disconnect_flags", disconnect_flags)
        if reason_code != 0:
            print("Unexpected disconnection. Reconnecting...")
        else:
            print("Client disconnected")
        # Attempt to reconnect if disconnected
        client.reconnect()
