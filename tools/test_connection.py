"""
Simple test that tries to connect to the mouse.
"""

from delux_m700.device import DeluxMouse


def main():

    mouse = DeluxMouse()

    print("Connecting...")

    if mouse.connect():

        print("Connected successfully!")

        print(mouse.device)

    else:

        print("Failed.")

    mouse.disconnect()


if __name__ == "__main__":
    main()
