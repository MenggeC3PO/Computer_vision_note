# Base image: Ubuntu 22.04
FROM ubuntu:22.04

# Update the package list and install the required dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    cmake \
    git \
    wget \
    unzip \
    pkg-config \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libgtk-3-dev \
    libcanberra-gtk* \
    libatlas-base-dev \
    gfortran \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    libxkbcommon-x11-0 \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages for Computer Vision
RUN pip3 install --upgrade pip
RUN pip3 install opencv-python opencv-contrib-python numpy matplotlib

# Set the username, user ID, and group ID
ARG UNAME=cv_user
ARG UID=1001
ARG GID=1001

# Define environment variables
ENV UNAME=${UNAME}

# Create a new group with the specified group ID and name
RUN groupadd -g $GID $UNAME

# Add a new user with the specified user ID and group ID
# The -m option creates a home directory for the user
# The -s /bin/bash sets the default shell to bash
RUN useradd -m -u $UID -g $GID -s /bin/bash $UNAME

# Set the password for the user and add the user to the sudo group
RUN echo "$UNAME:password" | chpasswd && adduser $UNAME sudo

# Set the working directory and fix permissions on the workspace directory as root
WORKDIR /home/$UNAME/CV_ws
RUN chown -R $UID:$GID /home/$UNAME/CV_ws

# Switch to the newly created user
USER $UNAME


# Expose necessary ports
EXPOSE 11011-11310
EXPOSE 11311

# Set the entrypoint to bash
CMD ["bash"]