#!/bin/bash
xhost +local:root

# Run the Docker container with the appropriate options
docker run -it \
    --rm \
    -v "$(pwd)/../CV_ws":/home/cv_user/CV_ws \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    $DEVICE_OPTION \
    --name="cv_container" \
    --network=host \
    cv_workspace bash


# if you need access to usb port with your container, add the follow line and change the port name
# --device=/dev/ttyACM0 \