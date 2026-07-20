"""
Open each HID interface of the Delux mouse and inspect it.

This script DOES NOT modify any mouse settings.
It only attempts to:

1. Open the interface.
2. Set a short read timeout.
3. Read a few HID reports.
4. Print what (if anything) is received.

This helps us identify which interface is used for normal mouse movement
and which may be used for configuration commands.
"""

import hid

VENDOR_ID = 0x30FA
PRODUCT_ID = 0x1440

TIMEOUT_MS = 500
READ_SIZE = 64

devices = hid.enumerate(VENDOR_ID, PRODUCT_ID)

print(f"\nFound {len(devices)} interface(s).\n")

for info in devices:

    print("=" * 80)
    print(f"Interface : {info['interface_number']}")
    print(f"Path      : {info['path']}")
    print("=" * 80)

    dev = hid.device()

    try:
        dev.open_path(info["path"])

        print("Opened successfully.")

        # Try reading three reports.
        for i in range(3):
            report = dev.read(READ_SIZE, TIMEOUT_MS)

            if report:
                print(f"Report {i + 1}:")
                print(report)
            else:
                print(f"Report {i + 1}: <no data>")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        try:
            dev.close()
        except Exception:
            pass

    print()
