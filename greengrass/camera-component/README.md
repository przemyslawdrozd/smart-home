
---
# Camera Component

## Prerequisites

### Give the greengrass permission for 
```bash
sudo visudo
```

### Add line to opened textfile
```ggc_user    ALL=(ALL:ALL) NOPASSWD: ALL```

### Create target directory for snapshots
```bash
sudo mkdir -p /greengrass/files/camera/
```

## 1. Setup Greengrass Deployment using GDK
```bash
cd /greenrass/camera-component
gdk build
gdk publish
```

## 2. Via AWS Console Revise deployment