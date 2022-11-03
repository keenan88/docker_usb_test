Startup Instructions:

Required software: Linux Ubuntu 22.04 and Docker 20.10.

Hardware:
1. Plug a USB mouse into your computer
2. Run $lsusb in the terminal. Find your mouse listed and take note of its Bus and Device number.
![image](https://user-images.githubusercontent.com/45887966/199812836-a879cbc8-5568-41e4-9f4a-8f34815b41bc.png)

3. Run $lsusb -D /dev/bus/usb/<YOUR MOUSE'S BUS ID>/<YOUR MOUSE'S DEVICE ID>. This will give you information about the device, including its vendor ID and product ID.
![image](https://user-images.githubusercontent.com/45887966/199812928-f51e65c6-f3be-433e-ab2c-cebdef8582e8.png)

4. cd to /dev/input/by-id and run $ls. Find and take note of your device.
![image](https://user-images.githubusercontent.com/45887966/199813764-3671499f-b935-4754-9892-01ceea4a5ad0.png)


Software:
1. Clone this repo
2. Open src/usbMouseTest.py and edit the idVendor and idProduct to be the same as the output from step 3 in the Hardware steps.
3. Open docker/docker-compose.yml and replace "usb-SINOWEALTH_Game_Mouse-if01-event-kbd" with the name of your device from step 4 in the Hardware steps (Note: "usb-SINOWEALTH_Game_Mouse-if01-event-kbd" occurs twice in the dockerfile, replace both occurances with your device name).
4. cd into docker_usb_test/docker
5. Run $docker compose up -d to build the container
6. Run $docker exec -it docker-docker_usb_test-1 bash to enter the container
7. cd into src and run python3 useMouseTest.py. As it runs, jiggle your mouse around.
9. You will see a bytestream of data print out to the terminal in a few seconds. If you do not jiggle your mouse, the read process may time out.
