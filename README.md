# PoC - RPI Camera module integrated with React Web App via AWS Greengrass & Amplify 
![smart-home-diagram drawio](https://github.com/user-attachments/assets/8edc7ba7-8cfc-4de3-8ebf-08c6326f345e)

#### The guide in 5 steps how from scratch
- **Setup RPI & Camera Component**
- **Connect via AWS CLI**
- **Create Greengrass device (Thing)**
- **Write and deploy custom component using GDK**

## Part 1 - Setup Rpi4 with Camera

This guide provides step-by-step instructions and troubleshooting during development.

### 1. Hardware Setup
1. **Attach the Camera**: 
   - Raspberry Pi is powered off.
   - Locate the CSI (Camera Serial Interface) port on the Raspberry Pi.
   
### 2. Update and Upgrade System

To ensure you have the latest software and firmware:
```bash
sudo apt update
sudo apt full-upgrade
```

### 3. Enable Camera Interface
Install & Enable the camera interface using the configuration:

```bash
sudo raspi-config
sudo apt install libcamera-apps
sudo reboot
```

### 4. Testing the Camera
```bash
libcamera-still -o test.jpg
```

## Part 2 - Setup RPI as Thing via Greengrass
### 1. Greengrass init from aws console
Install and Enter your AWS Access Key ID, Secret Access Key, region, and output format.

```bash
sudo apt install awscli -y
```
```bash
aws configure
```

### 2. Via AWS console -> Core Devices -> Set Up
Download & Run Installer on RPI
```bash
sudo apt install default-jdk -y
curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip > greengrass-nucleus-latest.zip && unzip greengrass-nucleus-latest.zip -d GreengrassInstaller
```
```bash
sudo -E java -Droot="/greengrass/v2" -Dlog.store=FILE -jar ./GreengrassInstaller/lib/Greengrass.jar --aws-region eu-central-1 --thing-name <thing_name> --thing-group-name G<thing_group_name> --component-default-user ggc_user:ggc_group --provision true --setup-system-service true --deploy-dev-tools true
```

## Part 3 - Setup GDK on Development OS 
Install GDK and init component to create custom components
```bash
python3 -m pip install -U git+https://github.com/aws-greengrass/aws-greengrass-gdk-cli.git@v1.6.2
```
```bash 
gdk component init
```
## Part 4 - How to use [GreengrassCameraComponent](greengrass%2Fcamera-component%2FREADME.md)

## Part 5 - [React Amplify Web App](greengrass%2Fcamera-component%2FREADME.md)
