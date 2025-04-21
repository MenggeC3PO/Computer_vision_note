# Computer Vision Docker Note

This repository is my personal note which contains a Docker-based development environment for computer vision projects, configured for Ubuntu 22.04 with Python, OpenCV, and AI libraries. 

## Repository Structure

- **docker/**:
   - **Dockerfile**: Configures the environment with OpenCV and essential libraries
   - **build_image.sh**: Creates the `cv_workspace` Docker image
   - **run_container.sh**: Launches the container with GUI support
   - **shell_container.sh**: Opens additional terminal shells into the running container
   
- **CV_ws/**: Workspace directory automatically mounted into the container for development

## Getting Started

1. **Build the Docker Image**:
    ```bash
    cd docker
    ./build_image.sh
    ```

2. **Launch the Container**:
    ```bash
    ./run_container.sh
    ```

3. **Access Additional Shells** (as needed):
    ```bash
    ./shell_container.sh
    ```

## Docker Configuration

To ensure proper permissions, add your user to the Docker group:

```bash
sudo usermod -aG docker $USER
```

Log out and log back in for the changes to take effect.

## About me

Mengge Zhang  
KU Leuven, Belgium  
Group T – Faculty of Engineering Technology  

[LinkedIn](https://www.linkedin.com/in/mengge-zhang-b474a8334/)