# Delux M700 Linux

A native Linux utility for configuring the Delux M700 / M700A gaming mouse.

## Goals

- DPI configuration
- Polling rate configuration (125/250/500/1000 Hz)
- RGB LED control
- Lightweight GUI
- No background service
- Linux Mint support

## Planned Tech Stack

- Python 3
- hidapi
- tkinter
- pyudev (optional)

## Status

🚧 Reverse engineering in progress.

Current work:

- [x] Windows software analyzed
- [x] USB traffic captured
- [ ] Decode HID reports
- [ ] Implement protocol
- [ ] CLI tool
- [ ] GUI