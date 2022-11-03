FROM osrf/ros:humble-desktop


# Python Requirements
RUN apt-get update \
    && apt-get install -y \
        python3 \
        python-is-python3 \
        pip\
      &&  pip install pyusb

RUN mkdir -p /ros_ws/src
WORKDIR /ros_ws
