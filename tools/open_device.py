"""
Open every Delux mouse HID interface individually.

This helps us determine which interface is the configuration interface.
"""

import hid
import pprint

VENDOR_ID = 0x30FA
PRODUCT_ID = 0x1440

devices = hid.enumerate(VENDOR_ID, PRODUCT_ID)

print(f"\nFound {len(devices)} matching HID interfaces\n")

for i, info in enumerate(devices, start=1):

    pprint.pp(info)

    print("=" * 70)

    print(f"Interface #{i}")

    print(f"Path      : {info['path']}")
    print(f"Interface : {info['interface_number']}")

    try:

        dev = hid.device()

        dev.open_path(info["path"])

        print("Opened successfully ✅")

        dev.close()

    except Exception as e:

        print("Failed ❌")

        print(e)
