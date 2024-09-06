# Setting Up a Local MQTT Broker with Mosquitto

### The MQTT Broke is needed for internal communication between component 

## Step 1: Install Mosquitto (MQTT Broker) on PRI4

```bash
sudo apt-get update
sudo apt-get install mosquitto mosquitto-clients
```

## Step 2: Run broker

```bash
sudo systemctl start mosquitto
```
