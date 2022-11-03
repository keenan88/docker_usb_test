import usb.core
from time import sleep

dev = usb.core.find(idVendor=0x258a, idProduct=0x1007)
ep = dev[0].interfaces()[0].endpoints()[0]
i = dev[0].interfaces()[0].bInterfaceNumber
dev.reset()

if dev.is_kernel_driver_active(i):
    print("detaching")
    dev.detach_kernel_driver(i)
    sleep(2)

print(dev.read(ep.bEndpointAddress, 1024))
