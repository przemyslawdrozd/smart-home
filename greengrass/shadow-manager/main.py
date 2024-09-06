
from src.ShadowManager import ShadowManager
from src.MqttPublisher import MqttPublisher
def main():
    try:
        print("Create mqtt publisher client")
        mqtt_client = MqttPublisher()
        print("Create Shadow Manager client")
        shadow_manager = ShadowManager(mqtt_client)

        print("Subscribe to Iot Core Topic")
        shadow_manager.subscribe_to_topic()

        print("Keep execution loop")
        shadow_manager.keep_loop_connection()

        print("Component closed!")

    except Exception as e:
        print("Error on main", e)


if __name__ == "__main__":
    main()
