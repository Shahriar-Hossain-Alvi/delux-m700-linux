"""
1. Detect the mouse.
2. Connect to it.
3. Disconnect safely.
4. (Later) Send HID reports.

The GUI, CLI, and protocol layers should NEVER talk to hidapi directly.
They will use this class.
"""

from __future__ import annotations
import hid
import traceback


class DeluxMouse:
    """
    Represents one connected Delux mouse.

    This class hides all hidapi details from the rest of the project.
    """

    # USB Vendor ID
    VENDOR_ID = 0x30FA

    # USB Product ID
    PRODUCT_ID = 0x1440

    def __init__(self) -> None:

        self.device: hid.device | None = None

    def connect(self) -> bool:
        """
        Open the HID device.

        Returns
        -------
        bool
            True if connection succeeded.
        """

        try:
            self.device = hid.device()

            if self.device is None:
                return False

            self.device.open(self.VENDOR_ID, self.PRODUCT_ID)

            return True

        except Exception:
            print(f"\nFailed to open device\n")
            traceback.print_exc()
            return False

    def disconnect(self) -> None:
        """
        Close the HID device.
        """

        if self.device is not None:

            self.device.close()

            self.device = None

    @property
    def is_connected(self) -> bool:

        return self.device is not None
