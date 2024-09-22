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

## Step 3: Connect with Shadow Document on cloud site
Add shadow document for thing and revise deployment with [aws.greengrass.ShadowManager](https://docs.aws.amazon.com/greengrass/v2/developerguide/shadow-manager-component.html?icmpid=docs_gg_console)

### Next step is to upload snapshot into S3 using sdk-component [sdk-component](https://github.com/przemyslawdrozd/smart-home/blob/16-add-readme/greengrass/sdk-component/README.md)
