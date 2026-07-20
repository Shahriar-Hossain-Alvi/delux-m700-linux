"""
This script lists every HID (Human Interface Device) connected to the computer.

Examples of HID devices:
- Mouse
- Keyboard
- Game Controller
- Drawing Tablet

We will use this script to locate our Delux M700 mouse and discover:

- Vendor ID (VID)
- Product ID (PID)
- Manufacturer
- Product Name
- Device Path

The device path will later be used to communicate with the mouse.
"""

import hid


def main():
    """
    Enumerate every HID device connected to the system.
    """

    devices = hid.enumerate()

    print(f"\nFound {len(devices)} HID device(s)\n")

    print("-" * 80)

    for index, device in enumerate(devices, start=1):

        print(f"Device #{index}")

        print(f"Vendor ID      : {hex(device['vendor_id'])}")
        print(f"Product ID     : {hex(device['product_id'])}")

        print(f"Manufacturer   : {device.get('manufacturer_string')}")
        print(f"Product        : {device.get('product_string')}")

        print(f"Serial Number  : {device.get('serial_number')}")

        print(f"Interface      : {device.get('interface_number')}")

        print(f"Usage Page     : {hex(device.get('usage_page', 0))}")
        print(f"Usage          : {hex(device.get('usage', 0))}")

        print(f"Path           : {device['path']}")

        print("-" * 80)


if __name__ == "__main__":
    main()
