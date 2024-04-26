---

# Network Packet Analyzer

The Network Packet Analyzer is a simple tool that allows users to capture and analyze network packets in real-time using Python and Tkinter.

## Features

- **Packet Capture**: Captures network packets in real-time.
- **Packet Analysis**: Analyzes captured packets and displays relevant information.
- **Start/Stop Control**: Allows users to start and stop packet capture at their convenience.

## Requirements

- Python 3.x
- Tkinter
- Scapy

## Installation

1. Install Python from the [official website](https://www.python.org/downloads/).
2. Install Tkinter using the command `pip install tk`.
3. Install Scapy using the command `pip install scapy`.

## Usage

1. Run the `packet_analyzer.py` script.
2. Click the "Start Capture" button to begin capturing network packets.
3. Click the "Stop Capture" button to stop capturing packets.
4. Analyze the captured packets displayed in the scrolled text area.

## Code Overview

The main script `packet_analyzer.py` contains the following components:

- `sniff_packet`: Function to continuously sniff network packets using Scapy.
- `update_list`: Function to update the packet list with captured packet information.
- `start_capture`: Function to start the packet capture process.
- `stop_capture`: Function to stop the packet capture process.
- Tkinter GUI components for the user interface: Start button, Stop button, and ScrolledText for displaying packet information.

## Credits

- Developed by Fakhur ul din.

## License

This project is licensed under the [MIT License](LICENSE).

--- 
