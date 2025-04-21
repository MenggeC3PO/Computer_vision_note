# ROS2 Humble Docker Template

This repo is the docker environment that I used for practicing computer vision on Ubuntu 22.04 with Python, OpenCV and AI. 

## Repository Overview

- **docker/**:
  - **Dockerfile**: Defines the base image with OpenCV and essential libraries. 
  - **build_image.sh**: Builds the Docker image as `cv_workspace`.
  - **run_container.sh**: Launches the container with GUI. 
  - **shell_container.sh**: Opens a new terminal shell into the running container
  
- **CV_ws/**: Computer vision workspace (auto-mounted into the container). All python code should save in here

## Quickstart

1. **Build the Image**: Go to `docker` and run:
   ```
   ./build_image.sh
   ```
2. **Start the Container**: From `docker`, execute:
   ```
   ./run_container.sh
   ```
3. **Additional Shell (Optional)**: For a new shell inside the running container, use:
   ```
   ./shell_container.sh
   ```

## Docker Permissions

Ensure your user has appropriate permissions by adding it to the Docker group:

```
sudo usermod -aG docker $USER
```

After executing the above command, you might need to log out and log back in for the group changes to take effect.


## Author
Mengge Zhang
KU Leuven, Belgium
Group T – Faculty of Engineering Technology